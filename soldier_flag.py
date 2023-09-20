import game_field_flag as game_field
import consts_flag as consts


# check if soldier's feet touch mine
def turtle_on_plastic_bag(x, y):
    if game_field.board[y][4+x] == consts.MINE or game_field.board[y+3][x] == consts.MINE_SHADOW:
        return True
    if game_field.board[y+1][4+x] == consts.MINE or game_field.board[y+3][x+1] == consts.MINE_SHADOW:
        return True
    return False


# check if soldier's feet touch flag
def turtle_on_seaweed(x, y):
    if game_field.board[y + 1][x+4] == consts.FLAG or game_field.board[y+3][x] == consts.FLAG_SHADOW:
        return True
    if game_field.board[y + 1][x+4] == consts.FLAG or game_field.board[y+3][x+1] == consts.FLAG_SHADOW:
        return True
    return False