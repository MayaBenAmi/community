import pygame
from screen import *
from clicks import *
from instructions import open_instructions
from main import recycle_vs_trash

pygame.init()






def play_happy_bunny():
    running = True
    while running:
        draw_game()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0]
                if check_x(mouse_x):
                    mouse_y = pygame.mouse.get_pos()[1]
                    if check_instructions_y(mouse_y):
                        open_instructions()
                    if check_recycle_y(mouse_y):
                        recycle_vs_trash()
                    # if check_catch_earth_y(mouse_y):
                    #     # open bubbles game
                    # if check_turtle_y(mouse_y):
                    #     # open the flag game
            if event.type == pygame.QUIT:
                running = False
            pygame.display.flip()

while True:
    play_happy_bunny()
