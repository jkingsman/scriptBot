#!/usr/bin/env python

import argparse
import twitter
import random
import time

parser = argparse.ArgumentParser()
parser.add_argument('lines', help='location of the lines file')
parser.add_argument('key', help='application key')
parser.add_argument('secret', help='application secret')
parser.add_argument('oauthtoken', help='oauth token')
parser.add_argument('oauth_secret', help='oauth secret')
parser.add_argument('interval', help='tweet interval in seconds')
args = parser.parse_args()

api = twitter.Api(consumer_key = args.key, consumer_secret = args.secret,
    access_token_key = args.oauthtoken, access_token_secret = args.oauth_secret)

print "Connected to twitter"

with open(args.lines) as lineFile:
    lines = lineFile.readlines()

print "Lines loaded"


def tweetLine():
    randLine = random.choice(lines)
    api.PostUpdate(status=randLine)
    print "Tweeted '" + randLine.strip('\n') + "'"
    time.sleep(int(args.interval))

while True:
    tweetLine()
