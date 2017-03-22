title: Python Readability Tricks
date: 2017-03-23
tags: [python]
category: blog
type: blog
summary: By breaking convention and lines, I find more clarity.
---
Almost all python programmers know the styleguides described in PEP8, and most seem to follow it at least to some extend. Some people follow it as hard rules others as guidelines, and sometimes it is even enforced via static analysis, I myself do that quite often with my code.

But I think that there is one principle that flows through PEP8, but is perhaps not stated in explicit terms: that the code should be readable and as easy to reason about as possible. By extension this means that the style presented in PEP8 is not hard and fast rules, but much more like guidelines, and perhaps they were originally intended as such.

This is not an original thought, this is something I have picked up over my years of writing python, and by watching a lot of talks about the topic. Notably from Raymond Hettinger, Brandon Rhodes and Erik Rose.

This idea and examples from the talks I have seen, have led me to develop my own habbits which does at times go against the letter of PEP8, but to me this set of practices improve the readability.

This is the PEP8 version of line splitting, and the one I encounter in the wild most frequently:

    :::python
    some_long_function(that_takes_lots_of_args=True, and_even_more_args=True,
                       extra_data=my_extra_data)

For some reasons I do not like the way the line is split, I have to scan for each argument. What I do instead is that I cut the line after each arg, and instead of indenting it to the open parenthesis that starts the call, just one level. This way each arg/kwarg becomes it own line, which I find very easy to read:

    :::python
    some_long_function(
        that_takes_lots_of_args=True,
        and_even_more_args=True,
        extra_data=my_extra_data,
    )

While on the topic, I also have a habbit of naming all my arguments, I find that it makes it clearer which argument/parameter/whatever does what. It is actually something I find lacking in most other programming languages, and probably one of the reasons I have not moved on from python as my primary hammer.

The same goes for when I write comprehensions, I split them:

    :::python
    new_list = [
        each
        for each in original_list
        if each
    ]

This way there are three lines in the list comphrehension that each serves its own purpose. The same goes for set and dict comprehensions as well as generator expressions.

The extra clarify becomes even more important, when I want to use a somewhat obscure trick, to flatten a nested list:

    :::python
    new_list = [
        each
        for sub_list in original_list
        for each in sub_list
        if each
    ]

Admittedly, these tricks generally involve being fairly liberal with the newlines, and thus making my code generally a bit longer than similar code written by others.

I hope that maybe someone finds this useful, and most is not completely against my cutting and slicing of python code.
