#!/Library/Frameworks/Python.framework/Versions/2.7/bin/python

import sys
import cgi

import cgitb; cgitb.enable()  # for troubleshooting

import random
import time
import argparse

def strTimeProp(start, end, format, prop):
    """Get a time at a proportion of a range of two formatted times.

    start and end should be strings specifying times formated in the
    given format (strftime-style), giving an interval [start, end].
    prop specifies how a proportion of the interval to be taken after
    start.  The returned time will be in the specified format.
    """

    stime = time.mktime(time.strptime(start, format))
    etime = time.mktime(time.strptime(end, format))

    ptime = stime + prop * (etime - stime)

    return time.strftime(format, time.localtime(ptime))


def randomDate(start, end, prop):
    return strTimeProp(start, end, '%m/%d/%Y', prop)

"""CHOMSKY is an aid to writing linguistic papers in the style
    of the great master.  It is based on selected phrases taken
    from actual books and articles written by Noam Chomsky.
    Upon request, it assembles the phrases in the elegant
    stylistic patterns that Chomsky is noted for.
    To generate n sentences of linguistic wisdom, type
        (CHOMSKY n)  -- for example
        (CHOMSKY 5) generates half a screen of linguistic truth."""

leadins = """
As predicted
Remember that
Don't forget
Media can't hide the fact that
Make sure you aren't misled -- 
Watch out --
Remember
Of course
Rubio ad claims
Cruz ad claims
Looks like
Because of me,





"""

# List of LEADINs to buy time.

subjects = """Megyn Kelly
Bimbo Megyn
Phony lawsuit against Trump U
POS WSJ WSJ LIAR FANTASY PUNDIT
Fox News
Fox News clown announcer
Failed presidential candidate Rand Paul
Weak RNC and Republican leadership
Ted Cruz
Cruz spokesperson
The failing @WSJ Wall Street Journal
@JebBush who wants COMMON CORE
The worthless @NYDailyNews
Little Mort Zuckerman
Lightweight Senator Marco Rubio
@MarkHalperin
@Morning_Joe
The Republican Establishment
Lightweight Marco Rubio
Mitt Romney, who was one of the dumbest and worst candidates in the history of Republican politics,
Jeb Bush
Hillary Clinton
One illegal
One of those Syrians
A Mexican
John Kasich, who nobody ever heard of,
@MittRomney
Another Romney advisor
Campaign mgr Stuart Stevens
"""

verbs = """is a Mitt Romney, who doesn't know how to win
does not have the right "temperment" to be President
totally panicked in firing his director of comm
has no chance to win Texas on Tuesday
has no chance to win Texas
has no chance to win Kansas
has no chance to win Ohio
has no chance to win in Florida
is a nasty guy, not one Senate endorsement and, despite talk, gets nothing done
should be disqualified from his fraudulent win in Iowa
is so wrong
is totally biased
wants COMMON CORE (education from D.C.)
is very weak on ILLEGAL IMMIGRATION ("come as act of love")
is a laughing stock -spent $100 million and is at bottom of pack
is a laughing stock
is a clown
is a complete failure
-- never shows up
has no buyers for what what they're selling
is frantically looking for relevance
is polling very poorly in Florida
-- the people can't stand him for missing so many votes
didn't win Iowa, he stole it
is very weak on illegal immigration
is very weak on Syria
is very weak on Middle East
lacks strength as illegals and Syrians pour in
lacks strength as dangerous aliens invade
accused me of using a very bad word
accused me of supporting Common Core
never built the greatest real estate empire in USA
has been pushing for lightweight Senator Marco Rubio to say anything to "hit" Trump
wants Rubio to "hit" me
forgot that I signed the pledge
is being mislead by the Cruz people
always chokes and this is no difference
is a choker, and once a choker, always a choker
is now pushing me on tax returns
wants to look cool, but it's far too late
is pathetic -- wants to look cool
spent more than $40,000,000 in New Hampshire to come in 4 or 5, I spent $3,000,000 to come in 1st
spent tons in Texas with nothing to show for it
is a disaster candidate who had no guts and choked
is a total joke, and everyone knows it
-- what a joke, it's clear to everybody
should get on the #TrumpTrain
-- another desperate move by someone who couldn't beat Hillary Clinton
"""

hashtag = """
#CaucusForTrump
#Trump2016  
#MakeAmericaGreatAgain
#VoteTrump
#VoteTrumpKS
#SuperTuesday
#CNNPoll
#donaldtrump
#gop
#trump
#repuplicans
#usa
#presidenttrump
#decision2016
#superSaturday
#asktrump





"""

interjections = """Bought and paid for
Don't know how to win  
Not a good messenger
Joke
Big difference in capability
1% in Nevada
A total loser
Don't allow it
BE CAREFUL
Total fabrication
Bad
Sad
Totally biased
Poor work ethic
Check the polls
Mr. Meltdown
Zero cred
Totally dishonest
It's dead
Lightweight
Lousy
Pathetic
What a liar
Not a leader
A pathetic figure
Dope
Choker
A real dummy
In the bag
WOW
Bought and paid for
Not a real person, right?
Faker
Phony"""



import textwrap, random
from itertools import chain, islice, izip
import re

closing = """</br>- Donald J. Trump (@realDonaldTrump) """ + str(randomDate("1/1/2016", "3/1/2016", random.random()))

def trump(times=2, line_length=72, closing=closing):
    parts = []
    for part in (leadins, subjects, verbs, ".", interjections, "!", hashtag):
        phraselist = map(str.strip, part.splitlines())
        random.shuffle(phraselist)
        parts.append(phraselist)
    output = chain(*islice(izip(*parts), 0, times))
    raw = textwrap.fill(' '.join(output), line_length)
    raw = raw.replace(" .", ".")
    raw = raw.replace(" !", "!")
    return raw + closing

def main(argv=None):
    '''this is called if run from command line'''
    parser = argparse.ArgumentParser()
    print trump(times=1, closing="")

# call main() if this is run as standalone
if __name__ == "__main__":
    sys.exit(main())
