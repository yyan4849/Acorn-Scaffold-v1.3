import sys
class Player:
    def __init__(self):
        self.display = 'A'
        self.num_water_buckets = 0
        self.row = 0
        self.col =  0
        self.old_row = 0
        self.old_col = 0

    def get_num_water_buckets(self,num):
        self.num_water_buckets = num

    def move(self, move):
        # movement conditions
        if move == 'w':
            self.row -= 1
            return 'w'
        elif move == "a":
            self.col -= 1
            return 'a'
        elif move == 's':
            self.row += 1
            return 's'
        elif move == 'd':
            self.col += 1
            return 'd'
        elif move == 'e':
            self.col
            self.row
            return 'e'
        elif move == 'q':
            print("\nBye!")
            sys.exit()
        else:
            return 'invalid'