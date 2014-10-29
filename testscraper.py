#!/usr/bin/env python
#testscraper.py

from scraper import Scraper

scraper = Scraper()
date = "20140301"
playerfile = "./data/TestPlayers.csv"
player_lines = scraper.ScrapeLines(date, playerfile)

# use simple count to verify test passed
playercount = len(player_lines)
if playercount == 6:
	print "Test PASSED!"
else:
	print "Test FAILED!"

print "Number of Players Lines Found:", playercount
print player_lines


