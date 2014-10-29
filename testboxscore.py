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
	player_line = bs.GetLine(box, player)
	return player_line

# test known passing case
testdate = "20140301"
testplayer = "L. James"
result = testboxscore(testdate,testplayer)
if result == "":
	print "Test failed"
else:
	print "Test passed:"
	print result

# test known failing case
testdate = "20140302"
testplayer = "L. James"
result = testboxscore(testdate,testplayer)
if result == "":
	print "Test passed"
else:
	print "Test failed:"
	print result



# NOTES:
# This now gets L. James and his stats! See below for example output.
# TO DO:
# 1. Refactor!
# ---- figure out how to minimize searching to only players in a given team. 
# -------- build a hash table to look up players / nba team
# 2. Figure out how to get player names to input
# ---- add a second class for players
# ---- do I need a class for STL teams?
# 3. Return output to web 

''' Example output
Player FOUND!
L. James</a></td>
<td class="shsTotD">F</td>
<td class="shsTotD">31:13</td>
<td class="shsTotD">8-12</td>
<td class="shsTotD">4-5</td>
<td class="shsTotD">0-2</td>
<td class="shsTotD">+14</td>
<td class="shsTotD">1</td>
<td class="shsTotD">9</td>
<td class="shsTotD">7</td>
<td class="shsTotD">0</td>
<td class="shsTotD">4</td>
<td class="shsTotD">2</td>
<td class="shsTotD">1</td>
<td class="shsTotD">20</td>
</tr>
'''

