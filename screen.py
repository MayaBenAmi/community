import consts
import pygame

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Happy Bunny")


def draw_catch_earth_button(catch_earth_img):
    catch_earth_button = pygame.image.load(catch_earth_img)
    sized_catch_earth = pygame.transform.scale(catch_earth_button, (consts.BUTTON_DIAMETER, consts.BUTTON_DIAMETER))
    screen.blit(sized_catch_earth, consts.CATCH_EARTH_BUTTON_LOCATION)


def screen_resize():
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def draw_turtle_button(turtle_img):
    turtle_button = pygame.image.load(turtle_img)
    sized_turtle = pygame.transform.scale(turtle_button, (consts.BUTTON_DIAMETER, consts.BUTTON_DIAMETER))
    screen.blit(sized_turtle, consts.TURTLE_BUTTON_LOCATION)


def draw_recycle_button(recycle_img):
    recycle_button = pygame.image.load(recycle_img)
    sized_recycle = pygame.transform.scale(recycle_button, (consts.BUTTON_DIAMETER, consts.BUTTON_DIAMETER))
    screen.blit(sized_recycle, consts.RECYCLE_BUTTON_LOCATION)


def draw_instructions_button(instructions_img):
    instructions_button = pygame.image.load(instructions_img)
    sized_instructions = pygame.transform.scale(instructions_button, (consts.BUTTON_DIAMETER, consts.BUTTON_DIAMETER))
    screen.blit(sized_instructions, consts.INSTRUCTIONS_BUTTON_LOCATION)


def draw_happy_bunny(happy_bunny_img):
    happy_bunny = pygame.image.load(happy_bunny_img)
    sized_happy_bunny = pygame.transform.scale(happy_bunny, (consts.BUNNY_WIDTH, consts.BUNNY_HIGHT))
    screen.blit(sized_happy_bunny, consts.BUNNY_LOCATION)


def draw_sad_bunny(sad_bunny_img):
    sad_bunny = pygame.image.load(sad_bunny_img)
    sized_sad_bunny = pygame.transform.scale(sad_bunny, (consts.BUNNY_WIDTH, consts.BUNNY_HIGHT))
    screen.blit(sized_sad_bunny, consts.BUNNY_LOCATION)


def draw_bushes(grass_img):
    grass = pygame.image.load(grass_img)
    sized_grass = pygame.transform.scale(grass, (100, 50))
    screen.blit(sized_grass, (300, 500))
    screen.blit(sized_grass, (600, 500))


def draw_game():
    screen.fill(consts.BG_COLOR)
    draw_catch_earth_button("catchearthdot.png")
    draw_turtle_button("turtledot.png")
    draw_instructions_button("instructionsdot.png")
    draw_recycle_button("recyclevstrash.png")
    draw_happy_bunny("happy_bunny.png")
    draw_bushes("grass.png")
    pygame.display.flip()
