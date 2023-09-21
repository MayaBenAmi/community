import sys

import pygame
import random
import datetime
import pickle
from screen import *
from clicks import *
from instructions import open_instructions
from main import recycle_vs_trash
from main_flag import flag
from main_catch_earth import catch_earth
from dyk import open_dyk
from dyk2 import open_dyk2
from dyk3 import open_dyk3
from dyk4 import open_dyk4
from dyk5 import open_dyk5

pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("main.mp3")

last_login = datetime.datetime.now()

if os.path.exists('data.pkl'):
    with open('data.pkl', 'rb') as fp:
        last_login = pickle.load(fp)
else:
    with open('data.pkl', 'wb') as fp:
        pickle.dump(last_login, fp)


def choose_random_dyk():
    dyk_choice = random.randint(1, 5)
    if dyk_choice == 1:
        open_dyk()
    elif dyk_choice == 2:
        open_dyk2()
    elif dyk_choice == 3:
        open_dyk3()
    elif dyk_choice == 4:
        open_dyk4()
    elif dyk_choice == 5:
        open_dyk5()


def play_happy_bunny():
    global last_login

    running = True
    while running:
        draw_game(last_login)
        for event in pygame.event.get():
            sound.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0]
                mouse_y = pygame.mouse.get_pos()[1]
                if check_x(mouse_x) and (check_instructions_y(mouse_y), check_recycle_y(mouse_y),
                                         check_catch_earth_y(mouse_y), check_turtle_y(mouse_y)):
                    if check_instructions_y(mouse_y):
                        open_instructions()
                        screen_resize()
                    if check_volume_y(mouse_y):
                        sound.stop()
                        draw_volume_on_button("sound.png")
                        screen_resize()
                    if check_recycle_y(mouse_y):
                        sound.stop()
                        recycle_vs_trash()
                        last_login = datetime.datetime.now()
                        choose_random_dyk()
                        screen_resize()
                    if check_catch_earth_y(mouse_y):
                        sound.stop()
                        catch_earth()
                        last_login = datetime.datetime.now()
                        choose_random_dyk()
                        screen_resize()
                    if check_turtle_y(mouse_y):
                        sound.stop()
                        flag()
                        last_login = datetime.datetime.now()
                        choose_random_dyk()
                        screen_resize()
            if event.type == pygame.KEYDOWN:
                with open('data.pkl', 'wb') as fp:
                    pickle.dump(last_login, fp)
                running = False
                sound.stop()
                pygame.quit()
                sys.exit()

            pygame.display.flip()


while True:
    play_happy_bunny()