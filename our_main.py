import pygame
from screen import *
from clicks import *
from instructions import open_instructions

pygame.init()

running = True
while running:
    draw_game()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



        if event.type == pygame.MOUSEBUTTONDOWN:
            mouse_x = pygame.mouse.get_pos()[0]
            if check_x(mouse_x):
                mouse_y = pygame.mouse.get_pos()[1]
                if check_instructions_y(mouse_y):
                    open_instructions()
                # if check_bubbles_y(mouse_y):
                #     # open bubbles game
                # if check_flag_y(mouse_y):
                #     # open the flag game
    pygame.display.flip()