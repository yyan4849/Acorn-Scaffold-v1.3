import sys
from cells import (
    Start,
    End,
    Air,
    Wall,
    Fire,
    Water,
    Teleport
)
CELLS_MAP = {
    'X': Start,
    'Y': End,
    ' ': Air,
    '*': Wall,
    'F': Fire,
    'W': Water,
}
# filename = sys.argv[1]
def read_lines(filename):
    try:
        f = open(filename)
    except FileNotFoundError:
        print("{} does not exist!".format(filename))
        sys.exit()
    lines = []
    while True:
        ln = f.readline()
        if ln == '':
            break
        stripped = ln.strip()
        lines.append(stripped)
    f.close()
    return lines
# print(read_lines(filename))

def parse(lines):
    x_count = 0
    y_count = 0
    grid = []
    teleport_count = {}
    for line in lines:
        line = line.strip()
        cell_line = []
        for char in line:
            if char == 'X':
                x_count += 1
            if char == 'Y':
                y_count += 1
            try:
                int(char)
                cell = Teleport(char)
                if char not in teleport_count:
                    teleport_count[char] = 1
                else:
                    teleport_count[char] += 1
            except ValueError:
                if char not in CELLS_MAP:
                    raise ValueError("Bad letter in configuration file: {}.".format(char))
                cell = CELLS_MAP[char]()
            cell_line.append(cell)
        grid.append(cell_line)

    if x_count != 1:
        raise ValueError("Expected 1 starting position, got {}.".format(x_count))
    if y_count != 1:
        raise ValueError("Expected 1 ending position, got {}.".format(y_count))
    for (key, value) in teleport_count.items():
        if value != 2:
            raise ValueError("Teleport pad {} does not have an exclusively matching pad.".format(key))
    return grid

def get_init_position(grid):
    for i, line in enumerate(grid):
            for j, cell in enumerate(line):
                    if type(grid[i][j]) == Start:
                        return [i,j]
# lines = read_lines(filename)
# print(parse(lines))