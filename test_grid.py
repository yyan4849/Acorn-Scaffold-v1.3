from grid import grid_to_string
import cells


def test_grid():
    class Player:
        def __init__(self):
            self.display = 'A'
            self.num_water_buckets = 0
            self.row = 0
            self.col =  0
        def get_num_water_buckets(self,num):
            self.num_water_buckets = num

    # test simple grid
    grid = [[cells.Wall(), cells.Start(), cells.Wall()],[cells.Wall(), cells.End(), cells.Wall()]]
    player = Player()
    expected = 'AX*\n*Y*\n\nYou have 0 water buckets.'
    actual = grid_to_string(grid, player)
    assert actual == expected, 'Simple test failed.'
    print("Simple test: passed!")

    # test grid with one water bucket
    grid_one_water =[[cells.Wall(), cells.Start(), cells.Wall(), cells.Water()],[cells.Wall(), cells.End(), cells.Wall(), cells.Wall()]]
    player.num_water_buckets = 1
    expected = 'AX*W\n*Y**\n\nYou have 1 water bucket.'
    actual = grid_to_string(grid_one_water, player)
    assert actual == expected, 'One water bucket failed.'
    print("One water bucket: passed!")

    # test grid with two water buckets
    grid_two_water = [[cells.Wall(), cells.Start(), cells.Wall(), cells.Water()],[cells.Wall(), cells.End(), cells.Wall(), cells.Water()]]
    player.num_water_buckets = 2
    expected = 'AX*W\n*Y*W\n\nYou have 2 water buckets.'
    actual = grid_to_string(grid_two_water, player)
    assert actual == expected, 'Two water bucket failed.'
    print("Two water bucket: passed!")

def run_tests():
    test_grid()

# run_tests()
