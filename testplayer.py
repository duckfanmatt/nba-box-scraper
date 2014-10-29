#!/usr/bin/env python
#testplayer.py

from player import Player
playerfile = "/home/mkhansen/projects/github/nba-box-scraper/data/Players.csv"
player = Player()
players = player.GetPlayers(playerfile)

print "Number of Players:",len(players)

for p in players:
	print p


