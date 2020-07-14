# hub-distance

Simple and lightweight commandline utility to determine the hub-distance of word.\
The hub-distance of a word `x` is defined over the minimum number of links needed to get from the wikipedia article to the pornhub domain.

## usage

Using `hub-distance` is as easy to use as pornhub is to google.

Just run:\
`main.py [WORD]` from the git root.

By default it'll print every site requested. \
If that is not to your liking change the code.

## known issues

`hub-distance` uses a depth-first search, so it will not finish
