import mimetypes
import os
from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from itertools import chain
from hashlib import md5

import boto3
import click
import csscompressor
import htmlmin
import markdown
import scarab
import yaml
from lxml import etree
from slugify import slugify
from watchdog.events import FileSystemEventHandler
from watchdog.observers import Observer


def parse_raw(page):
    metadata, content = page['raw'].split('---\n')
    page['content'] = content
    page['meta'] = yaml.load(metadata)
    if 'template' in page['meta']:
        page['template'] = page['meta']['template']
    else:
        page['template'] = page['meta']['type'] + '.html'
    return page


def add_html(page):
    if page['template'].endswith('.html'):
        page['html'] = markdown.markdown(
            page['content'],
            extensions=['markdown.extensions.codehilite'],
        )
        page['extension'] = 'html'
    elif page['template'].endswith('.atom'):
        page['extension'] = 'atom'
    return page


def add_destination(page):
    if 'destination' not in page['meta']:
        destination = page['meta']['url']
        destination = destination.lstrip('/')

        page['destination'] = os.path.join(destination, 'index.html')
    else:
        page['destination'] = page['meta']['destination']
    return page


def build_url(page):
    if 'url' not in page['meta']:
        page['meta']['slug'] = slugify(page['meta']['title'])
        url_pattern = '/{category}/{date.year}/{date.month}/{slug}/'

        page['meta']['url'] = url_pattern.format(**page['meta']).lower()

    return page


def resize_images(image):
    size = (800, 600)
    image['image'].thumbnail(size)
    return image


def make_images():
    images = scarab.loaders.image_loader('images')

    functions = (
        resize_images,
    )

    images = [
        run_functions(page, functions)
        for page in images
    ]

    for image in images:
        extension = os.path.splitext(image['path'])[1].lstrip('.')
        encoder = scarab.helpers.determine_encoder(extension)
        yield scarab.pages.Page(
            image['path'],
            scarab.helpers.image_to_bytes(
                image['image'],
                encoder,
            ),
        )


def run_functions(item, functions):
    for function in functions:
        item = function(item)
    return item


def asset_destination(asset):
    asset['destination'] = asset['path'][len('assets/'):]
    return asset


def css_compress(asset):
    if asset['destination'].endswith('.css'):
        asset['raw'] = csscompressor.compress(asset['raw'])
    return asset


def make_assets():
    assets = scarab.loaders.plaintext_loader('assets')
    functions = (
        asset_destination,
        css_compress,
    )

    assets = [
        run_functions(asset, functions)
        for asset in assets
    ]

    for asset in assets:
        yield scarab.pages.Page(
            asset['destination'],
            asset['raw'].encode(),
        )


def fill_projects(pages):
    projects_page = [
        each
        for each in pages
        if each['meta']['title'] == 'Projects'
    ][0]

    projects = defaultdict(list)
    for page in pages:
        if 'project' not in page['meta']:
            continue
        projects[page['meta']['project']].append(page)
    projects_page['subpages'] = projects


def fill_tags(pages):
    tags_page = [
        each
        for each in pages
        if each['meta']['title'] == 'Tags'
    ][0]

    tags = defaultdict(list)
    for page in pages:
        if 'tags' not in page['meta']:
            continue
        for tag in page['meta']['tags']:
            tags[tag].append(page)
    tags_page['subpages'] = tags


def fill_index(pages):
    index_page = [
        each
        for each in pages
        if each['meta']['title'] == 'Blog'
    ][0]

    index_page['subpages'] = [
        page
        for page in pages
        if page['meta']['type'] == 'blog'
    ]


def fill_feed(pages):
    feed_page = [
        each
        for each in pages
        if each['meta']['type'] == 'feed'
    ][0]

    feed_page['subpages'] = [
        page
        for page in pages
        if page['meta']['type'] == 'blog'
    ]


def make_content():
    pages = scarab.loaders.plaintext_loader('content')

    functions = (
        parse_raw,
        add_html,
        build_url,
        add_destination,
    )

    pages = [
        run_functions(page, functions)
        for page in pages
    ]

    # wow, I seriously need to find a generic way to make the subpages.
    fill_projects(pages)
    fill_tags(pages)
    fill_index(pages)
    fill_feed(pages)

    renderer = scarab.renderers.Renderer('templates')

    renderer.globals['site'] = {
        'domain': 'cknv.dk',
        'title': 'cknv',
    }
    renderer.globals['author'] = {
        'image': '/images/esben.jpg',
        'name': 'Esben Sonne',
        'email': 'esbensonne+blog@gmail.com',
    }
    renderer.globals['now'] = datetime.utcnow()

    renderer.filters['slug'] = lambda x: slugify(x)
    renderer.filters['isoformat'] = lambda x: x.strftime('%Y-%m-%dT%H:%M:%SZ')
    renderer.filters['simple_date'] = lambda x: x.strftime('%b %d %Y')

    parser = etree.XMLParser(remove_blank_text=True)

    for page in pages:
        rendered_page = renderer(page, page['template'])
        if page['extension'] == 'html':
            full_content = htmlmin.minify(rendered_page).encode()
        elif page['extension'] == 'atom':
            elem = etree.XML(rendered_page.encode(), parser=parser)
            full_content = etree.tostring(elem)

        yield scarab.pages.Page(page['destination'], full_content)


def set_mimetype(page):
    content_type, __ = mimetypes.guess_type(page.path)
    page['mimetype'] = content_type
    return page


def set_cache_control(page):
    cache_times_multipliers = {
        'image/jpeg': 12,
        'image/png': 12,
        'text/css': 12,
        'text/html': 5,
        'text/plain': 12,
        'application/atom+xml': 1,
    }

    cache_time = int(timedelta(minutes=5).total_seconds())

    multiplier = cache_times_multipliers[page['mimetype']]
    page['cache_control'] = 'max-age={}'.format(cache_time * multiplier)

    return page


def set_content_md5(page):
    page['content_md5'] = md5(page.bytes).hexdigest()
    return page


def all_things():
    yield from chain(
        make_content(),
        make_assets(),
        make_images(),
    )


@click.group()
def cli():
    pass


@cli.command()
def render():
    scarab.writers.bytes_writer(all_things(), 'output')


@cli.command()
def preview():
    server = scarab.servers.PreviewServer(8000)
    server.set_pages(all_things())

    class Updater(FileSystemEventHandler):
        def on_any_event(self, event):
            server.set_pages(all_things())

    updater = Updater()

    observer = Observer()
    folders = ('images', 'content', 'assets', 'templates')
    for each in folders:
        observer.schedule(updater, each, recursive=True)
    observer.start()

    try:
        print('Preview available at http://localhost:{}/'.format(8080))
        server.serve_forever()
    except KeyboardInterrupt:
        print('Shutting down...')
        server.shutdown()


@cli.command()
@click.option('--live', is_flag=True, help='Upload to live.')
@click.option('--force', is_flag=True, help='Ignore content checksums.')
def upload(live, force):
    functions = (
        set_mimetype,
        set_cache_control,
        set_content_md5,
    )

    items = [
        run_functions(item, functions)
        for item in all_things()
    ]

    s3 = boto3.resource('s3')

    if live:
        bucket_name = 'cknvdk'
    else:
        bucket_name = 'testcknvdk'

    print('uploading to: {}'.format(bucket_name))

    for item in items:
        s3_item = s3.Object(bucket_name, item.path)
        try:
            s3_item.load()
        except:

            print('uploading: {}'.format(item.path))
            s3_item.put(
                CacheControl=item['cache_control'],
                ContentType=item['mimetype'],
                Metadata={
                    'ContentMD5': item['content_md5'],
                }
            )
        else:
            existing_md5 = s3_item.metadata['contentmd5']
            new_md5 = item['content_md5']
            if not force and existing_md5 == new_md5:
                print('skipping: {}'.format(item.path))
                continue

            print('updating: {}'.format(item.path))
            s3_item.put(
                CacheControl=item['cache_control'],
                ContentType=item['mimetype'],
                Metadata={
                    'ContentMD5': item['content_md5'],
                }
            )


if __name__ == '__main__':
    cli()
