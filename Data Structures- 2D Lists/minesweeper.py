import random

# Mines and mine-free zones
mines_and_none = ["-", "#"]


# Generating random - or #
def coin_flip(mines_and_none):
    coin = random.choice(mines_and_none)
    return coin


# Creating the board
rows = 5
cols = 5

original_board = [[coin_flip(mines_and_none)
                   for _ in range(cols)] for _ in range(rows)]
for row in original_board:
    print(row)

# Filling - with number of # adjacent to it
mine_counter = 0
row_index = 0
col_index = 0


for row in original_board:
    # Starts column index over again
    col_index = 0
    for col in row:
        # Do nothing if value has a #
        if col == "#":
            col_index += 1
            continue
        # Scan surrounding values: if value has a -, add to mine counter
        elif col == "-":
            if row_index == 0:
                if col_index == 0:
                    if original_board[row_index][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index+1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
                if col_index == 4:
                    if original_board[row_index][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index-1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
                elif col_index < 4 and col_index > 0:
                    if original_board[row_index][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index-1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0

            if row_index == 4:
                if col_index == 0:
                    if original_board[row_index][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index+1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
                if col_index == 4:
                    if original_board[row_index][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index-1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
                elif col_index < 4 and col_index > 0:
                    if original_board[row_index][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index+1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
            elif row_index < 4 and row_index > 0:
                if col_index == 0:
                    if original_board[row_index-1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index+1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
                if col_index == 4:
                    if original_board[row_index-1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index-1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
                elif col_index < 4 and col_index > 0:
                    if original_board[row_index+1][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index+1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index-1] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index] == "#":
                        mine_counter += 1
                    if original_board[row_index-1][col_index+1] == "#":
                        mine_counter += 1
                    if original_board[row_index][col_index+1] == "#":
                        mine_counter += 1
                    original_board[row_index][col_index] = mine_counter
                    mine_counter = 0
            col_index += 1
    row_index += 1

print("\n")
for row in original_board:
    print(row)

'''
for row in original_board:
    print(str(row_index) + " row index")
    col_index = 0
    for col in row:
        print(str(col_index) + " col_index")
        col_index += 1
    print("New row")
    row_index += 1
'''
