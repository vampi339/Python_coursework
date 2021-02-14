import pickle
import random
from player import Player

class GUI:
    def clear():
        for x in range(50):
            print("\n")
    def display_stats(object):
        player = object
        print("total score: ", player.points, "\n"
              "player name: ", str(player.name), "\n"
              "total number of games: ", player.number_games, "\n")