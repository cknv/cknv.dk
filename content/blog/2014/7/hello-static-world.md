title: Hello Static World
date: 2014-07-14
tags: [meta]
category: blog
type: blog
project: beetle
summary: A little about this blog, what's under the hood and what I intend to write about.
---
Sorry, but this is mandatory. Welcome to what I intend to make a place for me to write - something that most people, including me, do far too little. So welcome to my blog - it is a static blog, which for the uninitiated means that there is no database and programming rendering the page as you request it, but rather the data and programming lies on my computer, than then renderers the html output once and puts it on a server for your reading.

Doing the heavy lifting is [beetle](https://github.com/cknv/beetle), which I wrote because I wasn't entirely happy with the existing options out there. [Some](https://github.com/mythmon/wok) came very close, but I was still a little unhappy with some of the (few) decisions it made.

So I wrote beetle, which is supposed to be quite simple and require little in the form of metadata in the actual pages. There are a few "reserved" keys in it, but otherwise it should be able to take any kind of new data and happily pass it on to the page rendering.

As an example I have given the site object a version number, there is no special support for this in the code, but it is handled any other property. The version is currently kept low, as the site is pretty spartan, consisting only of html, which may even be a little bit on the broken side.

Likewise, I have tried to steer away from implementing tags, but rather a generic grouping mechanism - since I wanted to both have a tag system, but also have a neat way of organising a series of posts about a project - that way, I can keep tags generic and have a project field in my posts. Which brings me to what I intend to write about.

I am a coder by trade, but I don't think I can limit myself to just writing about code, since one thing I enjoy a lot is to build stuff. Sure, one of the things I enjoy to build is software, and another is computers, but I also want to write about building a bike, something I have been thinking about doing for a couple of years now. So I expect that much of the content of this blog will in the series format, where I present something I want to do and later on how it's progressing.

This is actually one such post, and somewhere on the page you should see a link to the project "beetle" as that project is about building the software that runs this blog. I am sorry, I can't tell you where it is, since I may end up moving it around.

Lastly, as I began with, this is my place to write, something I am probably not very good at, but I would like to be better at. Surely my grammar is not perfect and I think I have an uncanny ability to form cludgy and too long sentences, hopefully I will learn and get better.
