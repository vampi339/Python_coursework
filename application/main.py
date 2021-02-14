from game import Game
from account import Account
from player import Player
import pickle


Account.accountDict = Account.load_account(Account.userDictName)
print(Account.accountDict)
Game.start()



