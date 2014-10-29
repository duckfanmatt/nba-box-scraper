#!/usr/bin/env python
#player.py

class Player(object):
	def __init__(self):
		return

	def GetPlayers(self, file):
		playerfile = open (file, "r")
		playerlist = []
		for player in playerfile:
			print "Player is:", player
			playerlist.append(player.strip('\n'))
		
		playerfile.close()

		return playerlist


