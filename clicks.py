import pygame
import consts

pygame.init()


# mouse_x = pygame.mouse.get_pos()[0]
# mouse_y = pygame.mouse.get_pos()[1]


def check_x(mouse_x):
    min_x = consts.INSTRUCTIONS_BUTTON_LOCATION[0]
    max_x = consts.INSTRUCTIONS_BUTTON_LOCATION[0] + consts.BUTTON_DIAMETER
    if min_x <= mouse_x <= max_x:
        return True
    else:
        return False


def check_instructions_y(mouse_y):
    min_y = consts.INSTRUCTIONS_BUTTON_LOCATION[1]
    max_y = consts.INSTRUCTIONS_BUTTON_LOCATION[1] + consts.BUTTON_DIAMETER
    if min_y <= mouse_y <= max_y:
        return True
    else:
        return False

def check_catch_earth_y(mouse_y):
    min_y = consts.CATCH_EARTH_BUTTON_LOCATION[1]
    max_y = consts.CATCH_EARTH_BUTTON_LOCATION[1] + consts.BUTTON_DIAMETER
    if min_y <= mouse_y <= max_y:
        return True
    else:
        return False


def check_turtle_y(mouse_y):
    min_y = consts.TURTLE_BUTTON_LOCATION[1]
    max_y = consts.TURTLE_BUTTON_LOCATION[1] + consts.BUTTON_DIAMETER
    if min_y <= mouse_y <= max_y:
        return True
    else:
        return False

def check_recycle_y(mouse_y):
    min_y = consts.RECYCLE_BUTTON_LOCATION[1]
    max_y = consts.RECYCLE_BUTTON_LOCATION[1] + consts.BUTTON_DIAMETER
    if min_y <= mouse_y <= max_y:
        return True
    else:
        return False

def check_volume_y(mouse_y):
    min_y = consts.VOLUME_BUTTON_LOCATION[1]
    max_y = consts.VOLUME_BUTTON_LOCATION[1] + consts.BUTTON_DIAMETER
    if min_y <= mouse_y <= max_y:
        return True
    else:
        return False