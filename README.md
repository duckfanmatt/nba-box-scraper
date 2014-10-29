nba-box-scraper
===============
Scrapes NBA game box scores and outputs individual player stats

Usage:
------
python scraper.py -f {filename} -d {date}  
	-d date in format yyyymmdd					
	-f file with list of player names

###example:
python scraper.py -f ./data/testplayers.txt -d 20141028

Test cases
----------
Simple test cases are included:
* testboxscore.py
* testplayer.py
* testscraper.py

###example:
python testscraper.py  
--> this should spit out "Test PASSED!" with a list of players found  

Player file format: 
-------------------
L. James  
D. Wade  
...  
D. Lillard  

###example file:
[data/testplayers.txt](data/testplayers.txt)

Known issues
------------
Currently this doesn't distinguish between players with the same first initial and last name. Ex: M. Plumlee could be Mason or Miles. User beware!




