import pygame
from screen import *
from clicks import *
from instructions import open_instructions
from main import recycle_vs_trash
from main_flag import flag
from main_catch_earth import catch_earth


pygame.init()
pygame.mixer.init()
sound = pygame.mixer.Sound("main.mp3")

def play_happy_bunny():
    running = True
    while running:
        draw_game()
        for event in pygame.event.get():
            sound.play()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x = pygame.mouse.get_pos()[0]
                if check_x(mouse_x):
                    mouse_y = pygame.mouse.get_pos()[1]
                    if check_instructions_y(mouse_y):
                        open_instructions()
                        screen_resize()
                    if check_recycle_y(mouse_y):
                        sound.stop()
                        recycle_vs_trash()
                        screen_resize()
                    if check_catch_earth_y(mouse_y):
                        sound.stop()
                        catch_earth()
                        screen_resize()
                    if check_turtle_y(mouse_y):
                        sound.stop()
                        flag()
                        screen_resize()
            if event.type == pygame.QUIT:
                running = False
                pygame.quit()
                sound.stop()
            pygame.display.flip()

running = play_happy_bunny()
while running:
    play_happy_bunny()
