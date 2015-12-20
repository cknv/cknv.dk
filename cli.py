import mimetypes
import os
from collections import defaultdict
from datetime import datetime
from datetime import timedelta
from itertools import chain

import boto3
import click
import markdown
import scarab
import yaml
from slugify import slugify


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
    page['html'] = markdown.markdown(page['content'])
    page['extension'] = 'html'
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
        yield {
            'destination': image['path'],
            'bytes': scarab.helpers.image_to_bytes(
                image['image'],
                encoder
            ).getvalue(),
        }


def run_functions(item, functions):
    for function in functions:
        item = function(item)
    return item


def asset_destination(asset):
    asset['destination'] = asset['path'][len('assets/'):]
    return asset


def make_assets():
    assets = scarab.loaders.plaintext_loader('assets')
    functions = (
        asset_destination,
    )

    assets = [
        run_functions(asset, functions)
        for asset in assets
    ]

    for asset in assets:
        yield {
            'destination': asset['destination'],
            'bytes': asset['raw'].encode(),
        }


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

    fill_projects(pages)
    fill_tags(pages)
    fill_index(pages)
    fill_feed(pages)

    renderer = scarab.renderers.Renderer(
        'templates',
        {
            'site': {
                'domain': 'cknv.dk',
                'title': 'cknv',
            },
            'author': {
                'image': '/images/esben.jpg',
                'name': 'Esben Sonne',
                'email': 'esbensonne+blog@gmail.com',
            },
            'now': datetime.utcnow(),
        }
    )

    renderer.filters['slug'] = lambda x: slugify(x)
    renderer.filters['isoformat'] = lambda x: x.strftime('%Y-%m-%dT%H:%M:%SZ')
    renderer.filters['simple_date'] = lambda x: x.strftime('%b %d %Y')

    for page in pages:
        yield {
            'destination': page['destination'],
            'bytes': renderer(page).encode(),
        }


def set_mimetype(item):
    content_type, __ = mimetypes.guess_type(item['destination'])
    item['mimetype'] = content_type
    return item


def set_cache_control(item):
    cache_times_multipliers = {
        'image/jpeg': 12,
        'image/png': 12,
        'text/css': 12,
        'text/html': 5,
        'text/plain': 12,
        'application/atom+xml': 1,
    }

    cache_time = int(timedelta(minutes=5).total_seconds())

    multiplier = cache_times_multipliers[item['mimetype']]
    item['cache_control'] = 'max-age={}'.format(cache_time * multiplier)

    return item


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
    import scarab
    cache = scarab.OutputCache('output')

    from watchdog.observers import Observer
    from watchdog.events import FileSystemEventHandler

    class Updater(FileSystemEventHandler):
        def on_any_event(self, event):
            scarab.writers.bytes_writer(cache.filter(all_things()), 'output')

    updater = Updater()

    observer = Observer()
    folders = ('images', 'content', 'assets', 'templates')
    for each in folders:
        observer.schedule(updater, each, recursive=True)
    observer.start()

    # from http import server
    # from socketserver import TCPServer

    # request_handler = server.SimpleHTTPRequestHandler

    # httpd = TCPServer(('', 8080), request_handler)
    print('started monitoring')
    import time
    try:
        # print('Preview available at http://0.0.0.0:{}/'.format(8080))
        # httpd.serve_forever()
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        # ...
        print('stopping monitoring...')
        # httpd.shutdown()


@cli.command()
@click.option('--test', default=True, help='upload to test bucket')
def upload(test):
    functions = (
        set_mimetype,
        set_cache_control,
    )

    items = [
        run_functions(item, functions)
        for item in all_things()
    ]

    s3 = boto3.resource('s3')
    if test:
        bucket_name = 'testcknvdk'
    else:
        bucket_name = 'cknvdk'

    print('uploading to: {}'.format(bucket_name))
    bucket = s3.Bucket(bucket_name)

    for item in items:
        bucket.put_object(
            Key=item['destination'],
            Body=item['bytes'],
            ContentType=item['mimetype'],
            CacheControl=item['cache_control']
        )
        print(item['destination'])


if __name__ == '__main__':
    cli()
