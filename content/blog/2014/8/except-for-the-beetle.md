title: Except for the beetle
date: 2014-08-22
project: beetle
category: blog
type: blog
summary: I was wrong, rather than pagination, beetle now has exceptions.
---
Beetle has exceptions!

I know, it sounds ridiculus. Why did it not have exceptions before? The answer to that is very simple: I was lazy. I had something that worked alright for me, and I was quite content. I had already scratched most of my proverbial itch.

Then one of my [co-workers](http://tenzer.dk) decided to have a look at beetle, and because there is no documentation or help or anything. He encountered a lot (I think all?) or the errors that beetle could produce. Luckily he did not give up, but rather delved into the code and began suggesting changes (via githubs pull request, for the initated), a lot of them made it into beetle and and is now in the canonical version (the master branch).

I suppose his suggestion to error handling was made making the minimum amount of changes to the code, and therefore they were just print statements, whenever beetle encountered an error or data that did not meet the prequisites. While I had no code to show for it, I had taken some thought to how I wanted beelte to handle errors, namely fail deadly. If *anything* goes wrong beetle should tell the user and quit, stopping whatever it was trying to do. No continuing, just fail. The reasoning is that I think a user is more likely to notice beetle failing to process a page rather than skipping it. And then it turn make it less likely that a incomplete/broken site gets uploaded.

Just notifying the user and continuing is a completely valid approach, and there was nothing wrong with it (I feel it is important to note), but it was just not the approach I wanted. But I had to write something different, rejecting an improvement (say, no error handling -> some error handling) without providing an alternative is just defenceless. So it did prompt me to write some error handling, and after some work, discussion and more work (repeated a few times) beetle now has a minimum of error handling.

Currently it just raises the exceptions, but they can tell you a bit about what is wrong, at some point the cli will be able to catch them and can then provide more useful information than just stacktraces.
