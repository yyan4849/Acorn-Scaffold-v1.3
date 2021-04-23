def grid_to_string(grid,player):
    string = ''
    # traverse the grid
    # if the grid.display is same as the cell.display turn grid into string
    for i, line in enumerate(grid):
        for j, cell in enumerate(line):
            if i == player.row and j == player.col:
                string += player.display
            else:
                string += cell.display
        string += '\n'
    # Take singular and plural into account
    if player.num_water_buckets == 1:
        string += '\nYou have {} water bucket.'.format(player.num_water_buckets)
    else:
        string += '\nYou have {} water buckets.'.format(player.num_water_buckets)
    return string