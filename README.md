nba-box-scraper
===============
Scrapes NBA game box scores and outputs individual player stats

Usage:
<python> scraper.py -f <player file> -d <date>
	-d date in format yyyymmdd"					
	-f file with list of player names

example:
python scraper.py -f ./data/testplayers.txt -d 20141028

Test cases
----------
Simple test cases are included:
testboxscore.py
testplayer.py
testscraper.py

example:
python testscraper.py
--> this should spit out "Test PASSED!" with a list of players found

Player file is of format: (see example as data/testplayers.txt)
--------------------------
L. James
D. Wade
...
D. Lillard

This currently expects first initial then last name in this format: L. James

Known issues
------------
Currently this doesn't distinguish between players with the same first initial and last name. Ex: M. Plumlee could be Mason or Miles. User beware!




