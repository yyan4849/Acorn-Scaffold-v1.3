import sys
from game import Game
# You may need this if you really want to use a recursive solution!
# It raises the cap on how many recursions can happen. Use this at your own risk!

filename = sys.argv[1]
mode = sys.argv[2]

parent = Game(filename)

def clone(parent):
    game = Game(filename)
    game.player = parent.player
    # parent = game

class Node:
    def __init__(self, gamestate):
        self.gamestate = gamestate
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.static = None

def DFS(node):
    nodes_list = [node]
    while True:
        if len(nodes_list) == 0:
            break

        node = nodes_list.pop(0)
        nodes_list = nodes_list[1:]

        # print(node.anime)

        if node.left:
            nodes_list.append(node.left)
        if node.right:
            nodes_list.append(node.right)
        if node.up:
            nodes_list.append(node.up)
        if node.down:
            nodes_list.append(node.down)
        if node.static:
            continue

def BFS(node):
    nodes_list = [node]
    while True:
        if len(nodes_list) == 0:
            break

        node = nodes_list.pop
        nodes_list = nodes_list[1:]

        # print(node.anime)

        if node.right:
            nodes_list.append(node.right)
        if node.left:
            nodes_list.append(node.left)
        if node.down:
            nodes_list.append(node.down)
        if node.up:
            nodes_list.append(node.up)
        if node.static:
            continue

def solve(mode):
    if mode == 'DFS':
        DFS()
    if mode == "BFS":
        BFS()


if __name__ == "__main__":
    solution_found = False
    if solution_found:
        solve(mode)
        print("### Config ###")
        print("string\n")
        print("\n### Output ###")
        print("Path has {} moves".format)
        print("Path:{}".format)
        # Print your solution...
    else:
        print("There is no possible path.")
