from game import Game
import os
import sys

name = sys.argv[1]

# filename no found
if len(name) == 0:
    print("Usage: python3 run.py <filename> [play]")
    sys.exit()
# create game object and set up the string map
game = Game(name)
game.return_grid()
game.set_player()
print(game.string())



# Play the game
while True:
    move = input("\nInput a move: ")
    # change upper case into lower case
    move = move.lower()
    game.game_move(move)
    print(game.string())
    if game.send_msg() != None:
        print(game.send_msg())
    if move not in ['a', 'w', 's' ,'d', 'e', 'q']:
        print("\nPlease enter a valid move (w, a, s, d, e, q).")