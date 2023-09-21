import pygame

import consts_catch_earth as consts

image = pygame.image.load('happy_bunny_new.png').convert_alpha()
rect = image.get_rect()
change_x = 0
change_y = 0
score = 0
points = ()
attack_bubbles = ()
prizes = ()


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()

    def update(self):
        self.rect.x += change_x
        self.rect.y += change_y

        # Check collision with wall
        if self.rect.left <= 0:
            self.rect.left = 0
        elif rect.right >= consts.WINDOW_WIDTH:
            self.rect.right = consts.WINDOW_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        elif self.rect.bottom >= consts.WINDOW_HEIGHT:
            self.rect.bottom = consts.WINDOW_HEIGHT


def init():
    rect.x = consts.PLAYER_START_X
    rect.y = consts.PLAYER_START_Y


def handle_input(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_LEFT:
            change_speed(-3, 0)
        elif event.key == pygame.K_RIGHT:
            change_speed(3, 0)
        elif event.key == pygame.K_UP:
            change_speed(0, -3)
        elif event.key == pygame.K_DOWN:
            change_speed(0, 3)
    elif event.type == pygame.KEYUP:
        if event.key == pygame.K_LEFT:
            change_speed(3, 0)
        elif event.key == pygame.K_RIGHT:
            change_speed(-3, 0)
        elif event.key == pygame.K_UP:
            change_speed(0, 3)
        elif event.key == pygame.K_DOWN:
            change_speed(0, -3)


def change_speed(x, y):
    global change_x
    global change_y

    change_x += x
    change_y += y


def check_collision(group):
    global score
    global my_player

    collide = pygame.sprite.spritecollide(my_player, group, True)
    if len(collide) != 0:
        if group == points:
            score += 1
        elif group == attack_bubbles:
            score -= 1


my_player = Player()
