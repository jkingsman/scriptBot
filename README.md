# scriptBot
Dump individual lines of dialogue from an SRT file.

Usage: `scriptBot srtFile MovieName [-d]`

The `-d` flag will delete the `srtFile` upon completion. scriptBot will create a folder named `MovieName` with the original script inside (`script.srt`) and the dialogue lines, one per line (`lines.txt`).
