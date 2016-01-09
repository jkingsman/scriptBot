# scriptBot

## Preparation
Dump individual lines of dialogue from an SRT file. [YIFY](http://www.yifysubtitles.com/) is a good source for these.

Usage: `prep.py srtFile `

Individual dialogue builds will be in `processed/MovieName.build`. **Protect this file - it has your twitter credentials in plaintext.**

## Tweeting
Tweet a random line per the settings in a built dialog file.

Usage: `tweet.py builtDialog`
