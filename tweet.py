#!/usr/bin/env python

import argparse
import twitter
import random
import time
import json

parser = argparse.ArgumentParser()
parser.add_argument('buildfile', help='built line file location')
args = parser.parse_args()

with open(args.buildfile) as buildfile:
    builtObject = json.load(buildfile)

print "Lines loaded"

api = twitter.Api(consumer_key = builtObject['key'], consumer_secret = builtObject['secret'],
    access_token_key = builtObject['oauthtoken'], access_token_secret = builtObject['oauthsecret'])

print "Connected to twitter"

def tweetLine():
    randLine = random.choice(builtObject['lines'])
    try:
        api.PostUpdate(status=randLine)
        print "Tweeted '" + randLine.strip('\n') + "'"
        time.sleep(int(builtObject['interval']))
    except:
        # 99% of the time, this is a duplicate tweet
        print "Skipping duplicate/error"
    

print "Tweeting lines from", builtObject['title'], "every", builtObject['interval'], "seconds"

while True:
    tweetLine()
