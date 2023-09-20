import consts_flag as consts
import random

board = []


# create empty board matrix
def build_board():
    global board

    board = []
    for i in range(consts.ROW_NUM):
        row = []
        for j in range(consts.COL_NUM):
            row.append(consts.EMPTY)
        board.append(row)


# adds any object and its shadow to empty space in matrix
# shadow is the space the object takes in matrix
def add_object(obj, num_of_objects, size, shadow):
    for cnt in range(num_of_objects):
        found_empty_pos = False
        while not found_empty_pos:
            x = random.randint(0, consts.COL_NUM - 1 - size[0])
            y = random.randint(0, consts.ROW_NUM - 1 - size[1])
            occupied = False
            for i in range(x, x + size[0]):
                for j in range(y, y + size[1]):
                    if board[j][i] != consts.EMPTY:
                        occupied = True
            if occupied:
                continue
            found_empty_pos = True
            for i in range(x, x + size[0]):
                for j in range(y, y + size[1]):
                    board[j][i] = shadow
            board[y][x] = obj


def add_mines():
    add_object(consts.MINE, consts.NUM_OF_MINES, consts.PLASTIC_BAG_SIZE, consts.MINE_SHADOW)


def add_grass():
    add_object(consts.GRASS, consts.NUM_OF_GRASS, consts.BUBBLES_SIZE, consts.GRASS_SHADOW)


def add_flag():
    x = consts.COL_NUM - consts.SEAWEED_SIZE[0] - 1
    y = consts.ROW_NUM - consts.SEAWEED_SIZE[1] - 1
    for i in range(consts.SEAWEED_SIZE[0]):
        for j in range(consts.SEAWEED_SIZE[1]):
            board[y + j][x + i] = consts.FLAG_SHADOW
    board[y][x] = consts.FLAG