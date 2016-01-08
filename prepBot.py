#!/usr/bin/env python

import argparse
import os
import shutil
import pysrt
import re

parser = argparse.ArgumentParser()
parser.add_argument('srt', help='srt location')
parser.add_argument('name', help='movie name')
parser.add_argument('--length', default=8, help='minimum length of line')
parser.add_argument('--delete', action='store_true', help='delete original')
args = parser.parse_args()

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
        if len(splitLine) > args.length:
            brokenLines.append(splitLine)

lineFile = open('processed/' + args.name + '-lines.txt', 'w')
lineFile.write('\n'.join(brokenLines))
lineFile.close()

print "Script dumped;", len(brokenLines), "lines"

if args.delete:
    os.remove(args.srt)
