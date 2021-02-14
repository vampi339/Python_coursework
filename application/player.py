import pickle
import random

class Player(object):

    def __init__(self, name, points, number_games, number_rocks, number_paper, number_scissors):
        self.name = name
        self.points = points
        self.number_games = number_games
        self.number_rocks = number_rocks
        self.number_scissors = number_scissors
        self.number_paper = number_paper

    def return_name(self):
        return str(self.name)

    def print_stats(self):
        print (self)
    # a function to save player instances. used in AQccount.signup() function
    def save_player(obj, name):
        with open('obj/player_saves/' + name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    # a function to load player instances. used in Account.login() function
    def load_player(name):
        with open('obj/player_saves/' + name + '.pkl', 'rb') as f:
              return pickle.load(f)