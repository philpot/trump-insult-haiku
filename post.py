#!/usr/bin/env python

#-----------------------------------------------------------------------
# twitter-post-status
#  - posts a status message to your timeline
#-----------------------------------------------------------------------

# from twitter import *
from twitter import Twitter, OAuth
from tweet import trump

#-----------------------------------------------------------------------
# what should our new status be?
#-----------------------------------------------------------------------
new_status = None
while not new_status:
    new_status = trump(times=1, closing="")
    if len(new_status) >= 140:
        new_status = None

#-----------------------------------------------------------------------
# load our API credentials 
#-----------------------------------------------------------------------
config = {}
# This should be related to __file__
execfile("/home/andrewphilpot/project/trump-insult-haiku/config.py", config)

#-----------------------------------------------------------------------
# create twitter API object
#-----------------------------------------------------------------------
twitter = Twitter(
    auth = OAuth(config["access_key"], config["access_secret"], config["consumer_key"], config["consumer_secret"]))

#-----------------------------------------------------------------------
# post a new status
# twitter API docs: https://dev.twitter.com/docs/api/1/post/statuses/update
#-----------------------------------------------------------------------
results = twitter.statuses.update(status = new_status)
