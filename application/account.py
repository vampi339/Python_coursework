import pickle
import random
import os
from player import Player

class Account:
    userDictName = "userdict"  # variable that stores the name of the file with the accounts
    accountDict = {}

    def accountPrint():
        a = 0

    # accountDict =  {"vampi339":"123", "mogatata":"1213"}
    # for x,y in accountDict.items():
    #    print(x, " : ", y)

    # Works. should add more interactivity
    def login():
        print("LOGIN:")
        is_found = False  # a bool that indicates weather the username is found in the dict, so that a statemant "username does not exists" can be made
        is_account = input("do you have an account? Y/N")
        if (is_account == "N" or is_account == "n"):
            Account.singup()
        elif (is_account == "Y" or is_account == "y"):
            username = input("please enter a username: [1]")
            password = input("please enter a password: ")

            for x, y in Account.accountDict.items():
                if (username == x):
                    print("username is found !")
                    is_found = True

                    if (password == y):
                        print("login succsessful !")
                        return username
                        break

                    elif (password != y):
                        print("wrong password !")
                        return -1
            if (not is_found):
                print("the username does not exists !")  # the statement is after the loop for a reason. do not move
                return -1
        else:
            print(" you did not enter a valid option. Please try again !")
            return -1

    # works
    def singup():
        print("SIGN UP: ")
        username = input("please enter a username: [0]")
        password = input("please enter a password: ")
        tryagain = False  # bool that is changed upon already existing name
        # check if username exists
        for x, y in Account.accountDict.items():
            if (username == x):
                print("username already exists.Please try again")
                tryagain = True
                Account.singup()
        # if username does not exists, add username and password to dictionary
        if (not tryagain):
            Account.accountDict[username] = password
            # Player.save_player(username)  # adds a save file with the player's name that holds all the stats
            print("you have made an account successfuly")
            Account.save_account(Account.accountDict,
                                 Account.userDictName)  # add the new account to the dict with accounts
            player = Player(str(username), 0, 0, 0, 0, 0)  # create a new player and saving him
            Player.save_player(player, username)
            print(Account.accountDict)
            Account.login()

    def save_account(obj, name):
      #  path = 'obj/' + str(name)
       # os.makedirs(path)
        with open('obj/' + name + '.pkl', 'wb') as f:
            pickle.dump(obj, f, pickle.HIGHEST_PROTOCOL)

    def load_account(name):
        with open('obj/' + name + '.pkl', 'rb') as f:
            return pickle.load(f)

