title: New Linux Install
date: 2014-10-08
tags: [arch linux, diy]
category: blog
type: blog
summary: I finally pulled myself together and made my laptop as fancy as my workstation at work.
---
For a long time, my laptop have had an old version of Linux Mint on it and to be honest, I was not great. It had some quirks and the underlying Ubuntu system made the whole thing a bit heavy to my taste.

Recently, I installed [Arch Linux](https://archlinux.org) on my computer at work, and that worked wonders. Although it is a much simpler machine. There is no need to deal with WiFi, suspend and hibernate, media buttons and other essencially "weird" stuff. I say weird because I have always had difficulties with getting all the components working together to a nice and managable system.

So I decided that I was fed up having old version of software on my machine, I wanted Python 3.4, I wanted to try Haskell and/or Rust, and I wanted to do that without tracking down a decent ppa, and without forcing it into the sytem. So it was time for a change.

### Things have really changed

Getting Arch installed was a breeze, I remember installing Arch back in the day when they had a [TUI](http://en.wikipedia.org/wiki/Text-based_user_interface) to help you along, and right after they dropped it. And I recall it suddently being really hard to be able to finish an install, but luckily, some tooling have sprung up in place of the TUI. Which makes it a little less manual to finish the install.

Getting it up and running is easy and then follows installing all the packages you need, I decided to use [Cinnamon](http://en.wikipedia.org/wiki/Cinnamon_(software)), which is still a heavy environment, but thanks to the lightweight Arch core, it is not so bad.

I had some problems with my WiFi, but I found out that it is a bad idea to have both the NetworkManager and the dhcpcd service running at the same time, they seemed to conflict somewhat.

One issue remains, the fonts looks ugly, but that is a story for another day.
