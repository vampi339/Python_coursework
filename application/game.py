from account import Account
from player import Player
from gui import GUI
import random

class Game:

    def print_rules():
        print("Welcome !")
        print("this is a game of rock, paper scisors. the rules are as follows:\n")
        print("you chose one of the following options:\n"
              "1. rock\n"
              "2. paper\n"
              "3. scissors\n"
              "using the numbers 1, 2 and 3 choose the correspondent item. rock beats scissors, scissors \n"
              "beat paper and papre beats rock.. after that you press enter.\n"
              "the game has already decided what to move to make by the time you make your choice.\n"
              "But keep in mind that the game remembers the choices you make and acts in correspondence to that.\n"
              "with other words, the more you play the harder it gets.\n"
              "lets START !\n")
    def bot_move():
        return random.randrange(1,3)
    def recognize_move(pawn):
        return{
            1 : "rock",
            2 : "paper",
            3 : "scissors"
        }[pawn]

    def start():
        choice = Account.login()
        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",choice)
        while (choice == -1):
            print("please try again")
            choice = Account.login()
        player = Player.load_player(str(choice))

        Game.print_rules()
        score = 0


        gameon = "Y"
        while (gameon == "Y"):

            result = ""
            bot_move = Game.bot_move()  # int that shows the move of the bot and is used to decide who wins
            bot_movement = Game.recognize_move(bot_move)  # used in print functions
            player_move = int(input("choose a number in range from 1 to "
                                    "3 \n"
                                    "1. rock\n"
                                    "2. paper\n"
                                    "3. scissors\n"))
            print("bot choice: ", bot_movement)
            print("your choice: ", Game.recognize_move(player_move))

            if(bot_move == player_move):
                result = "tie"
                player.number_games += 1
            elif( bot_move == 1 and player_move == 2):
                result = "YOU WIN"
                player.number_paper += 1
                player.points += 1
                player.number_games +=1
                score += 1
            elif (bot_move == 1 and player_move == 3):
                result = "YOU lOSE"
                player.number_scissors += 1
                player.number_games += 1
            elif (bot_move == 2 and player_move == 1):
                result = "YOU lOSE"
                player.number_rocks += 1
                player.number_games += 1
            elif (bot_move == 2 and player_move == 3):
                result = "YOU WIN"
                player.number_scissors += 1
                player.number_games += 1
                player.points += 1
                score += 1
            elif (bot_move == 3 and player_move == 1):
                result = "YOU WIN"
                player.number_rocks += 1
                player.number_games += 1
                player.points += 1
                score += 1
            elif (bot_move == 3 and player_move == 2):
                result = "YOU lOSE"
                player.number_paper += 1
                player.number_games += 1
            print(result)

            gameon = input("do you wish to play again ? Y/N \n")


        GUI.display_stats(player)
        Player.save_player(player, Player.return_name(player))

