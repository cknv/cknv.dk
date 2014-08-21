title: Plugins! Glorious plugins!
date: 2014-08-13
project: beetle
category: blog
type: blog
summary: Been a while since I wrote last, something was bothering me.
---
The last few times I have been sitting down to try and write something in this blog, I have been distracted. Distracted by myself wanting to rewrite the code that renders this page to be much, much nicer.

Basically, I have been rewriting the overall structure to inject dependencies (although I am not sure if it qualifies for following the dependency injection pattern), the various parts are then exposed to all plugins that the user care to install and use. I removed my local test server, and rewrote it as a plugin, plugged it in, lo and behold it works.

Likewise I have been writing a plugin that can upload the entire output to S3, which happens to be where I host this blog. In addition it can also gzip the content and set whatever headers you want to on the files - like cache-control.

The markdown support in the engine has also been removed, and implemented in a plugin. I do not want to dictate what format posts are written in, so implement your own! Write one for rst, one for textile, one for yaml (dispite it's name) or hell you could even write your own markup language and do it yourself.

The plugins are where all the functionality that not everyone needs - hence the name. I want to put my files on S3 gzipped, but not everyone needs that. Maybe someone just wants rsync the whole output to their server or put it on github pages. Just because I want to put my stuff on S3 I should still make it possible (even easy) for other people to use alternatives. The plugins are where I allow myself to be opinionated and pick specifics and not just implement what I hope everybody needs.

In short I am much much happier with how the engine works, and although I still think it needs a lot more refactoring to do something about the nasty/inconsistent internals, but at least the user facing parts are getting better.

Next up is probably pagination, since the front page of this blog is getting kind of long.
