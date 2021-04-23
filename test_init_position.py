from game_parser import get_init_position
import cells


def test_init_position():
    grid_1 = [[cells.Wall(), cells.Start(), cells.Wall()],[cells.Wall(), cells.End(), cells.Wall()]]
    actual = get_init_position(grid_1)
    excepted =[0,1]
    assert actual == excepted, 'Init player 1 failed'
    print("Init player 1: passed!")

    grid_2 = [[cells.Wall(), cells.Wall(), cells.Start()],[cells.Wall(), cells.End(), cells.Wall()]]
    actual = get_init_position(grid_2)
    excepted =[0,2]
    assert actual == excepted, 'Init player 2 failed'
    print("Init player 2: passed!")

    grid_3 = [[cells.Wall(), cells.Wall(), cells.Wall()],[cells.Start(), cells.End(), cells.Wall()]]
    actual = get_init_position(grid_3)
    excepted =[1,0]
    assert actual == excepted, 'Init player 3 failed'
    print("Init player 3: passed!")


def run_tests():
    test_init_position()
# run_tests()
