#!/usr/bin/env python
#testscraper.py

from scraper import Scraper

scraper = Scraper()
date = "20140301"
playerfile = "./data/testplayers.txt"
playerlines = scraper.ScrapeLines(date, playerfile)

# use simple count to verify test passed
playercount = len(playerlines)

print "Number of Players Lines Found:", playercount
print playerlines

if playercount == 6:
	print "Test PASSED"
else:
	print "Test FAILED"

