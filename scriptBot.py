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

if not os.path.exists(args.name):
    os.makedirs(args.name)

shutil.copyfile(args.srt, args.name + '/script.srt')
subs = pysrt.open(args.name + '/script.srt')
subTexts = [sub.text for sub in pysrt.open(args.name + '/script.srt')]


def lineScrubber(line):
    line = line.replace('<i>', '').replace('</i>', '')
    line = line.replace('\n', ' ')
    line = line.replace('- ', '')
    return line

brokenLines = []
for line in map(lineScrubber, subTexts):
    splitLines = re.split('\? |\! |(?<!Mr)(?<!Mrs)\. ', line)
    for splitLine in splitLines:
        if len(splitLine) > args.length:
            # add it with non-ascii stripped
            brokenLines.append("".join(i for i in splitLine if ord(i) < 128))

lineFile = open(args.name + '/lines.txt', 'w')
lineFile.write('\n'.join(brokenLines))
lineFile.close()

print "Script dumped;", len(brokenLines), "lines"

if args.delete:
    os.remove(args.srt)
