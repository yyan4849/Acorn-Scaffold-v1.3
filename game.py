import sys
from game_parser import read_lines, parse, get_init_position
from grid import grid_to_string
from player import Player
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)


class Game:
    def __init__(self, filename):
        self.filename = filename
        self.player = Player()

        self.grid = []
        self.lines = None

        self.cell = None

        self.move = None
        self.move_record = ' '
        self.move_counter = 0

    def return_grid(self):
        # get the cell grid map
        self.lines = read_lines(self.filename)
        self.grid = parse(self.lines)

    def game_move(self, move):
        # change upper case into lower case
        # receive the move input and call the corresponding cell step method
        try:
            self.player.old_col = self.player.col
            self.player.old_row = self.player.row
            self.move = self.player.move(move)
            if self.move == 'invalid':
                self.cell = Air()
                return
            else:
                self.cell = self.grid[self.player.row][self.player.col]

        except IndexError:
            self.cell = Wall()
        if self.player.col < 0 or self.player.row < 0:
            self.cell = Wall()
        self.cell_action = self.cell.step(self)



    def send_msg(self):
        # conditions on different cells
        return self.cell.msg

    def string(self):
        # print the string
        string = grid_to_string(self.grid, self.player)
        return string

    def set_player(self):
        # call the function make A start at X
        co = get_init_position(self.grid)
        self.player.row = co[0]
        self.player.col = co[1]
        self.player.old_col = self.player.col
        self.player.old_row = self.player.row