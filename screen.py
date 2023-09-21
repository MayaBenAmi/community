import consts
import pygame
import pickle
import datetime
import os

screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))
pygame.display.set_caption("Bunny To The Rescue")


def draw_catch_earth_button(catch_earth_img):
    catch_earth_button = pygame.image.load(catch_earth_img)
    sized_catch_earth = pygame.transform.scale(catch_earth_button, (consts.BUTTON_DIAMETER, consts.BUTTON_DIAMETER))
    screen.blit(sized_catch_earth, consts.CATCH_EARTH_BUTTON_LOCATION)


def screen_resize():
    screen = pygame.display.set_mode((consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))

def draw_volume_off_button(volume_off_button_img):
    volume_off_button = pygame.image.load(volume_off_button_img)
    sized_volume_off_button = pygame.transform.scale(volume_off_button, (50,50))
    screen.blit(sized_volume_off_button, consts.VOLUME_BUTTON_LOCATION)

def draw_volume_on_button(volume_on_button_img):
    volume_on_button = pygame.image.load(volume_on_button_img)
    sized_volume_on_button = pygame.transform.scale(volume_on_button, (50, 50))
    screen.blit(sized_volume_on_button, consts.VOLUME_BUTTON_LOCATION)


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

def welcome_text(text_img):
    text = pygame.image.load(text_img)
    sized_text = pygame.transform.scale(text ,(400, 120))
    screen.blit(sized_text, (300,70))


# last_login = 0
# with open('person_data.pkl', 'wb') as fp:
#     pickle.dump(last_login, fp)
def draw_game(last_login):
    screen.fill(consts.BG_COLOR)
    welcome_text("text.png")
    draw_volume_off_button("nosoundupd.png")
    draw_catch_earth_button("catchearth.png")
    draw_turtle_button("turtledot.png")
    draw_instructions_button("instructionsdot.png")
    draw_recycle_button("recyclevstrash.png")
    draw_bushes("grass.png")
    draw_happy_bunny("happy_bunny.png")

    current_time = datetime.datetime.now()
    time_difference = current_time - last_login
    hour_difference = time_difference.total_seconds() / 3600
    if hour_difference > 24:
        draw_sad_bunny("sad_bunny.png")
    else:
        draw_happy_bunny("happy_bunny.png")
    pygame.display.flip()
