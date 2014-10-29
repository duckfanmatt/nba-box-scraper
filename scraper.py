#!/usr/bin/env python
#scraper.py
from boxscore import BoxScore
from player import Player
import sys, getopt

class Scraper(object):
	def __init__(self):
		# init code here
		return

	def ScrapeLines(self,date, playerfile):
		player_lines = []
		player = Player()
		players = player.GetPlayers(playerfile)
		
		if len(players) == 0:
			print "ERROR - No players found"
			return ""
		else:
			print "Number of Players:",len(players)
		
		# Get the links to the boxscores from the scoreboard
		bs = BoxScore()
		scoreboard = bs.GetScoreboard(date)
		links = bs.GetLinks(scoreboard)

		if len(links) == 0:
			print "ERROR - No links found on scoreboard"
			return ""
		
		player_lines = self.GetPlayerLines(bs, links,players)
		return player_lines

	def GetPlayerLines(self, bs, links, players):
		player_lines = []		
		# Open each links URL and search for player
		for link in links:
			URL = bs.GetLinkURL(link)
			if URL == "":
				print "ERROR empty URL at link:", link
				next(link)
			print "Processing URL:", URL
			box = bs.GetBox(URL)
			for p in players[:]: # iterate over COPY of players list
				line = bs.GetLine(box, p)
				
				# if line > 0 player was found
				# is this needed if the line is ""?
				if len(line) > 0:
					print "Saving", p," stat line"
					# add the player line
					player_lines.append(line)
					# don't search for the player again
					print "Removing", p," from search"
					players.remove(p) # remove from players list
					print "remaining players: ",players
		return player_lines

	
def usage():
	print "usage: scraper.py -f -d"
	print "-d date in format yyyymmdd"					
	print "-f file with list of player names"



def main(argv):
	# parse args -- could be moved to a separate function
	try:
		opts, args = getopt.getopt(argv,"hf:d:",["file=","date="])
   	except getopt.GetoptError:
		self.usage()
      		sys.exit(2)
  	for opt, arg in opts:
      		if opt == '-h':
         		self.usage()
         		sys.exit()
      		elif opt in ("-f", "--file"):
         		infile = arg
      		elif opt in ("-d", "--date"):
         		date = arg
   	# do scraping
	scraper = Scraper()
	player_lines = scraper.ScrapeLines(date, infile)
	print "Players Lines Found:"
	for line in player_lines:
		print line

if __name__ == "__main__":
	main(sys.argv[1:]) # pass in cmd line args
		

			
