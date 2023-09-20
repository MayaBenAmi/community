import consts_flag as consts
import pygame

# create screen
screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def init_image(filename, size):
    img = pygame.image.load(filename)
    return pygame.transform.scale(img, (consts.SQUARE_LEN * size[0], consts.SQUARE_LEN * size[1]))


# displaying images on screen
def draw_grass(x, y):
    screen.blit(bubbles_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_flag(x, y):
    screen.blit(seaweed_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_mine(x, y):
    screen.blit(plastic_bag_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


def draw_soldier(soldier):
    y = soldier[0]
    x = soldier[1]
    screen.blit(turtle_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))



def draw_explode(soldier):
    y = soldier[0]
    x = soldier[1]
    screen.blit(explotion_image, (x * consts.SQUARE_LEN, y * consts.SQUARE_LEN))


# displaying massage on screen
def draw_game_over(msg):
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    txt_image = font.render(msg, True, consts.FONT_COLOR)
    txtRect = txt_image.get_rect()
    txtRect.center = (consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2)
    screen.blit(txt_image, txtRect)


# main screen function
def draw_game(board, soldier, show_mines, explode):
    pygame.display.set_caption("Turtle on A Mission")
    screen.fill(consts.BACKGROUND_COLOR)
    # loop goes over every cell in matrix, checks if there is an object
    # if there is: displays the object on screen
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == consts.GRASS:
                draw_grass(x, y)
            elif board[y][x] == consts.FLAG:
                draw_flag(x, y)
            # if player presses 'enter' screen changes to dark mode and displays mines
            if show_mines and board[y][x] == consts.MINE:
                            draw_mine(x, y)
    # if soldier explodes: screen displays an explosion
    if explode:
        draw_explode(soldier)
    else:
        draw_soldier(soldier)


# initializing images
bubbles_image = init_image(consts.IMG_BUBBLES, consts.BUBBLES_SIZE)
seaweed_image = init_image(consts.IMG_SEAWEED, consts.SEAWEED_SIZE)
plastic_bag_image = init_image(consts.IMG_PLASTIC_BAG, consts.PLASTIC_BAG_SIZE)
turtle_image = init_image(consts.IMG_TURTLE, consts.TURTLE_SIZE)
explotion_image = init_image(consts.IMG_DEATH, consts.TURTLE_SIZE)