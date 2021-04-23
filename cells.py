import sys

def WaterToAir(grid, game):
    # define function change water cell into air cell
    for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                if grid[i][j].display == 'W' and game.col == j and game.row == i:
                    row = grid[i]
                    row[j] = Air()
                    grid[i] = row
                    return

def FireToAir(grid, game):
    # define function change fire cell into air cell
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if grid[i][j].display == 'F' and game.col == j and game.row == i:
                row = grid[i]
                row[j] = Air()
                grid[i] = row
                return

class Start:
    def __init__(self):
        self.display = 'X'
        self.msg = None

    def step(self, game):
        game.move_counter +=1
        game.move_record += game.move + ', '


class End:
    def __init__(self):
        self.display = 'Y'
        self.msg = None

    def step(self, game):
        # update the move attribute same below
        game.move_counter += 1
        game.move_record += game.move
        print(game.string())
        print("\n\nYou conquer the treacherous maze set up by" \
            " the Fire Nation and reclaim the Honourable Furious"\
                " Forest Throne, restoring your hometown back to its former glory"\
                 " of rainbow and sunshine! Peace reigns over the lands.")
        if game.move_counter == 1:
            print("\nYou made 1 move.")
            print("Your move:{}\n".format(game.move_record))
        else:
            print("\nYou made {} moves.".format(game.move_counter))
            print("Your moves:{}\n".format(game.move_record))
        print("=====================\n====== YOU WIN! =====\n=====================")
        sys.exit()



class Air:
    def __init__(self):
        self.display = ' '
        self.msg = None

    def step(self, game):
        game.move_counter +=1
        game.move_record += game.move + ', '


class Wall:
    def __init__(self):
        self.display = '*'
        self.msg = None

    def step(self, game):
        # push back the player
        game.player.row = game.player.old_row
        game.player.col = game.player.old_col
        self.msg = "\nYou walked into a wall. Oof!"


class Fire:
    def __init__(self):
        self.display = 'F'
        self.msg = None

    def step(self, game):
        FireToAir(game.grid, game.player)
        game.move_counter +=1
        # different conditions for step into a fire
        if game.player.num_water_buckets > 0:
            game.move_record += game.move + ', '
            self.msg = "\nWith your strong acorn arms, you throw a water bucket at the fire. "\
                "You acorn roll your way through the extinguished flames!"
            game.player.num_water_buckets -=1

        else:
            game.move_record += game.move
            print(game.string())
            print ("\n\nYou step into the fires and watch your dreams disappear :(.\n")
            print("The Fire Nation triumphs! The Honourable Furious Forest is reduced to a pile of"\
                " ash and is scattered to the winds by the next storm... You have been roasted.")
            if game.move_counter == 1:
                print("\nYou made 1 move.")
                print("Your move:{}\n".format(game.move_record))
            else:
                print("\nYou made {} moves.".format(game.move_counter))
                print("Your moves:{}\n".format(game.move_record))
            print("=====================\n===== GAME OVER =====\n=====================")
            sys.exit()



class Water:
    def __init__(self):
        self.display = 'W'
        self.msg = None

    def step(self, game):
        WaterToAir(game.grid, game.player)
        game.move_counter +=1
        game.move_record += game.move + ', '
        game.player.num_water_buckets += 1
        self.msg = "\nThank the Honourable Furious Forest, you've found a bucket of water!"

class Teleport:
    def __init__(self, display):
        self.display = display
        self.msg = None


    def step(self, game):
        game.move_counter +=1
        game.move_record += game.move + ', '
        self.msg = "\nWhoosh! The magical gates break Physics as we know it and opens a wormhole through space and time."
        # search for the teleport partner and update the player cordinator
        for i, line in enumerate(game.grid):
            for j, cell in enumerate(line):
                if game.cell.display == game.grid[i][j].display and (game.player.col != j or game.player.row != i):
                    game.player.row = i
                    game.player.col = j
                    return

