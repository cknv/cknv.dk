title: Watercooled M1
date: 2015-12-22
tags: [builds, mini-itx, watercooling]
project: NCase M1 V2
category: blog
type: blog
summary: Watercooling a toaster (sized) pc.
---
A while ago I ran into a problem with my pc, it began overheating when I was playing some of the newer games. Since the hardware is pretty recent, and of "enthusiast" grade, I was pretty certain that it was not a performance problem, but rather just a problem with getting rid of the heat the system generated.

This was probably due to how the hardware is layout in the case. A 780 ti in a NCase M1, more or less acts like a divider and separates the case into a upper and a lower part. As it was the lower part did not have any fans exchanging the air, so it would just build up. I had previously tried to fit in some case fans, to feed fresh air directly into the GPU. But the fans ended up touching and thus blocking one of the GPU fans (causing the other to spin up to 100%, which was very noisy). Long story short, the lower part was pretty much closed off, so the air the GPU was using the cool with was the air it was heating, over and over and over, causing it to get hotter and hotter. Which is of course hardly ideal.

So I went and made a spreadsheet with all the parts I would need to watercool my pc. I went with EK blocks, 16/10 Tygon Norprene tubing, Alphacools ST30 radiator, two Noctua NF-12 PWM, and a Laing DDC pumb in the bottom. For the reservoir I had previously bought the [NCase M1 reservoir](http://www.frozenqshop.com/m1-ncase-reservoir/), and the whole thing got filled up with distilled water accompanied by a silver kill coil from Mayhems.

The planning and buying process was not easy, I had to do a lot of reading, to learn what is generally recommended, but also what do people like me with very small cases do. Luckily there is a fair amount of enthusiasts out there with NCase M1s, so I was able to look at pictures, part lists, and forums and learn a lot about what would be possible. Some TechTubers also proved valuable, especially [Jay](https://www.youtube.com/user/Jayztwocents) proved helpful with the how-to videos, especially for getting the GPU block in place, as I have never taken any GPU apart before.

The plan was to make a very low maintenance water loop, and with the combination of Norprene tubing, distilled water, and silver, I think I have actually managed to pull it off - although, only time will actually tell. So far I have only needed to top up the reservoir after most of the air bled out, and the water remains crystal clear, but then again, it has less than two months.

I had at first bought some random no-brand fittings, but as I was actually building, they began causing problems with how little space I had to work with. So I went ahead and tried to find something different, and refound the Bitspower fittings, which I had originally counted out due to them simply being weird. Coming back to them, I realized that they are not individual fittings, but rather a system to build your own fittings with - which was perfect for me, as there is some tight bends and turns in the routing that thick walled tubes was not quite able to follow.

Since I was anyway rebuilding my pc, I also switched to the Silverstone 600W SFX power supply, which there is not much to say about, while perhaps one of the most important parts of a system, the power supply is also one of the least sexy.

### Results

And it works beautifully, mostly. The pc no longer overheats, while it runs a little hot, it is not too bad. It is also a good deal quieter, except for the pump: The PWM controls on the DDC pump works (after some troubles setting it up), but since it is PWM controlled the speed goes a little up or down, despite my best effords to keep it at a constant speed. This is then aggravated by the fact that the pc is on my desk, right next to me, any noise is very noticable.

### Next time...

While I have managed to watercool my first pc, I did notice somethings I would like to do different next time I am to build a watercooled pc. First off, I have realized that while I like the size of the NCase M1, building a watercooled pc in it, becomes very, very tight. Currently in order to change anything inside the pc, I have to disassemble it partly. Next time, I think I might want to go for a [caselabs](http://caselabs-store.com) case, but that might require an appartment that is slightly bigger than what I currently live it, but no rush, I want USB type-c connectors on the front panel anyway. I also do not know exactly which case I prefer. I think the full sized ATX towers is overkill for me, as I probably will not need more than a mATX board, but caselabs does not make it easy to pick a case: they have *so* many options.

With regards to the pump I have later found the D5 Vario pump, which seems like a very easy choice of pump, as it should provide a very consistent pump performance, which of course goes hand in hand with consistent noise, something I found the PWM DDC is struggling with. However, D5 pumps are a bit larger than DDCs, so I will have to wait until I have that larger case.

I am also considering that, next time, if there is space for it, I could put in quick disconnects between all major components. In order to make it easier to take the system apart to change something. It will be a lot of quick disconnects but it will mean that there is no need to drain the system if I want to change a part.

All in all, I watercooled my first pc, it was fun, and I will do it again.
