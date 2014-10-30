#!/usr/bin/env python
#testboxscore.py
import re
from boxscore import BoxScore

def testboxscore(date, player):
	bs = BoxScore()

	scoreboard = bs.GetScoreboard(date)
	links = bs.GetLinks(scoreboard)
	if len(links) == 0:
		exit()
	else: 
		link = str(links[0])	

	print "first link:",link

	URL = bs.GetLinkURL(link)

	box = bs.GetBox(URL)
	playerline = bs.GetLine(box, player)
	return playerline

# test known passing case
testdate = "20140301"
testplayer = "L. James"
result = testboxscore(testdate,testplayer)
if result == "":
	print "Test FAILED"
else:
	print result
	print "Test PASSED"
	

# test known failing case
testdate = "20140302"
testplayer = "L. James"
result = testboxscore(testdate,testplayer)
if result == "":
	print "Test PASSED"
else:
	print result
	print "Test FAILED"


