title: The Point of Zero Upgradeability
date: 2014-07-16
project: A PC for A
tags: [builds, mini-itx]
type: blog
category: blog
summary: Getting started with planning a SFF build for a friend.
---

So one thing I said I enjoyed was to build computers, and as a part of that I seem to be "that guy" (or at least one of "those guys") that my friends go to whenever they need to have their PC upgraded - although I don't do everything. My general recommandation to problematic windows machines have been "install linux", so that kind of requests stopped fairly quickly.

But I digress. I have a friend (we're going to call her A) who got burned on buying a stationary, assuming that all stationaries can be upgraded. When she was complaining a little that it was not very good at pulling some MMO I had hardly heard about I promised to pop it open and have a look inside.

I was surprised, this thing was the size of a midi-tower, but the actual board seemed to be a mini-itx, with no PCI slots and a Ivy Bridge Celeron CPU - which is not bad, just noway near what she wanted/needed. I gueess if you strip out the optical disk drive and find a smaller HDD, the whole thing could be VESA mounted on the back of her screen. But what surprised me the most was probably that there was no PSU inside the case, but a 12V DC input on the IO Panel, and when I asked, the PSU was indeed an external powerbrick, like you normally get with a laptop. I think this was a bit of lazy design from the manufacturer, since there was so much empty space in the cabinet, you could easily have fitted a small PSU in there.

Needless to say, there is practically no upgrade path with that PC, at least not an easy one.

After I delivered the diagnosis, we began talking about what else could be done. Given that I had just build a computer for her boyfriend and I seem to be one of the hardware interested guys at work (we are about 20 nerds in development), I offered my help with building her a PC.

As far as I understood the main requirements are:

* Better graphics performance.
* Upgradeability.
* Small footprint (her desk is not big).

And everybody likes:

* A nice looking case.
* Low maintenance.
* Silence.

I am thinking she falls into the low/mid range gamer class, and thus there is no need for a dual GPU setup or watercooling, or many of those fancy things, small and simple can do fine. With regards of upgradeability, that term may perhaps even be in quotes, as the main need here is a single PCI-Express slot so it can fit a replaceable GPU. A good CPU would be in order as the computer as a whole can then live through a couple of generations of GPU upgrades.

So given that I am already partial to SFF PCs, I thought that she can do fine with a mini-itx pc - hell the beta Steamboxes are mini-itx. So I sent her a list a few different mini-itx and mATX cases to kind of get a starting point for the discussion.

It would seem that the IN WIN 901 is in the lead currently, the runner up was the BitFenix Prodigy, but the case width kind of ruled it out - that desk size making things hard. I liked the Thermaltake Core V1, recently announced at Computex in Taipei, but it's not out yet, and who knows how long it takes for it to reach Europe?

From what I have already read, the IN WIN 901 appears to be a fine case, for a *certain* kind of build. It has very little room for fans, so getting the heat of the case requires a bit of thought - and some powerful fans. The other notable problems are storage mounting, and price, but heat can be dealt with with proper thought, the need for storage is anyway kind of limited, so the case fits fine. I could forsee a problem with the price, but we already have a spreadsheet for all the parts. To make it easy to spot if a part costs too much and breaks the budget.

###Futher research

There is still some things I need to research, in order to progress with this plan.

First I need to familiarize myself with AMDs APU chips and how much performance they can yield - I know it's not top of the line, but is it good enough? If it is then it could change the direction of the build, from the traditional Intel + GPU build to an APU build - which would be new territory and thus kind of interesting to do.

If it's not enough, then how well will a GPU cool in this case? EVGAs ACX cooler does a very good job of removing heat from the 750 (ti?) from what I understand, it's actually overkill, but I could certainly keep the GPU cool. Although I have thought that the cooler might suffer from another kind of issue in this case: it exhausts to the sides, which may lead to a buildup of hot air inside the case. A rear exhausted GPU could alliviate this, but I have yet to actually see a 750 (or similar level) GPU with a rear exhaust, but I haven't looked very thoroughly, so I may just have missed it.
