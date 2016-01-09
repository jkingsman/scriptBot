#!/usr/bin/env python

import argparse
import os
import shutil
import pysrt
import re
import json

parser = argparse.ArgumentParser()
parser.add_argument('srt', help='srt location')
args = parser.parse_args()

title = raw_input("Movie name: ")
lineLength = raw_input("Min line length: ")
interval = raw_input("Seconds between tweets: ")
key = raw_input("Application key: ")
secret = raw_input("Application secret: ")
oauthtoken = raw_input("OAuth token: ")
oauthsecret = raw_input("OAuth secret: ")

subTexts = [sub.text for sub in pysrt.open(args.srt)]

def lineScrubber(line):
    line = line.replace('<i>', '').replace('</i>', '')
    line = line.replace('\n', ' ')
    line = line.replace('- ', '')
    # scrub non-ascii
    line = "".join(char for char in line if ord(char) < 128)
    return line

brokenLines = []
for line in map(lineScrubber, subTexts):
    splitLines = re.split('\? |\! |(?<!Mr)(?<!Mrs)\. ', line)
    for splitLine in splitLines:
        if len(splitLine) > int(lineLength):
            brokenLines.append(splitLine)

movieData = {}
movieData['title'] = title
movieData['key'] = key
movieData['secret'] = secret
movieData['oauthtoken'] = oauthtoken
movieData['oauthsecret'] = oauthsecret
movieData['interval'] = interval
movieData['lines'] = brokenLines

lineFile = open('processed/' + title + '.build', 'w')
lineFile.write(json.dumps(movieData))
lineFile.close()

print "Script dumped;", len(brokenLines), "lines"
