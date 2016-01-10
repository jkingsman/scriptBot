# scriptBot
Tweet random lines from movie dialogues, sourced subtitle files.


## Preparation
Dump individual lines of dialogue from an SRT file. [YIFY](http://www.yifysubtitles.com/) is a good source for these.

Usage: `prep.py srtFile `

Individual dialogue builds will be in `processed/MovieName.build`. **Protect this file - it has your twitter credentials in plaintext.**

## Tweeting
Tweet a random line per the settings in a built dialog file.

Usage: `tweet.py builtDialog`

## Make your own bot

1. Make a twitter account
2. Get your API keys
  * [Make an app](https://apps.twitter.com/app/new)
  * Go to the *Keys and Access Tokens* tab
  * Generate an access token
  * The keys are listed on the page in the order that `prep.py` asks for them (consumer key, consumer secret, access/oauth token, access/oauth secret)
3. Get a sub file (I recommend [YIFY](http://www.yifysubtitles.com/))
4. Run `prep.py [yoursubfile]`
  * Provide title, minimum length, interval, and API keys as requested
5. Start tweeting: `tweet.py processed/yourMovieFile.build`
  * You can put it in the backgroun on a *nix system with `nohup python tweet.py processed/yourMovieFile.build &`
