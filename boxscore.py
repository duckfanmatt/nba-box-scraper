#!/usr/bin/env python
#boxscore.py

import requests
from bs4 import BeautifulSoup
import re
import string

class BoxScore(object):
	def __init__(self):
		# scoreboard url
		self.url = 'http://stats.oregonlive.com/nba/scoreboard.asp'

	def GetScoreboard(self, date):
		# get the scoreboard page
		if (date > 0):
			url = self.url+"?day="+str(date)
		else:
			url = self.url
		
		page = requests.get(url)

		# clean it for easy parsing
		scoreboard = BeautifulSoup(page.text)
		return scoreboard
	
	def GetLinks(self, scoreboard):
		# find all the box score links
		links = scoreboard.find_all(href=re.compile("boxscore"))
		if len(links) == 0:
			print "ERROR -- No Box Scores found"

		return links

	def GetLinkURL(self, link):
		result = re.search('href="(.*)">Box', str(link))
		if result: 
			URL = re.sub(r'/nba/.*',result.group(1), self.url)
			print "Link URL=",URL
		else:
			print "ERROR in GetLinkURL - href not found\n"
			URL=""
		return URL

	def GetBox(self, link):
		boxscore = []		
		page = requests.get(link)
		if not(page):
			print "ERROR - couldn't get page at link - ", link
			return boxscore

		# clean for easy parsing
		cleanpage = BeautifulSoup(page.text)
		
		# find boxscore within page
		boxscore = cleanpage.find_all("tr", class_=re.compile("shsRow[0,1]Row"))
		if len(boxscore) == 0:
			print "ERROR - couldn't find box score on page at link - ", link
		return boxscore;
		 	
	def GetLine(self, boxscore, player):
		print "Searching for player - ", player
		playerline = ""
		for statline in boxscore:
			playersearch = str(player)+r'</a></td>(.*)</tr>'
			result = re.search(playersearch, str(statline), re.DOTALL)
	
			if result:
				playerline = CleanLine(result.group())
				print "Player ",player, "FOUND!"
				break # player found, don't need to keep looking
				
		if playerline == "":
			print "Warning -", player, "not found"
			
		return playerline


def CleanLine(playerline):
	# clean up HTML line and return only data
	# input looks like this:
	'''
	T. Chandler</a></td>
	<td class="shsTotD">C</td>
	<td class="shsTotD">27:45</td>
	<td class="shsTotD">4-8</td>
	<td class="shsTotD">0-0</td>
	<td class="shsTotD">0-0</td>
	<td class="shsTotD">-8</td>
	<td class="shsTotD">3</td>
	<td class="shsTotD">10</td>
	<td class="shsTotD">0</td>
	<td class="shsTotD">0</td>
	<td class="shsTotD">2</td>
	<td class="shsTotD">1</td>
	<td class="shsTotD">5</td>
	<td class="shsTotD">8</td>
	</tr>
	'''
	cleanline = []	
	result = re.search(r'(.*)</a></td>', playerline) # player name
	if result:
		print "Player name:", result.group(1)
		cleanline.append(result.group(1))
	
	print "Line = ", playerline
	result = re.findall(r'<td class="shsTotD">(.*)</td>', playerline) # player stats
	for stat in result:
		cleanline.append(stat)
	
	print "Player stats:", cleanline

	return cleanline


