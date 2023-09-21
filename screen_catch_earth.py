import consts_catch_earth as consts
import pygame

screen = pygame.display.set_mode(
    (consts.WINDOW_WIDTH, consts.WINDOW_HEIGHT))


def screen_init():
    pygame.display.set_caption('Catch Earth')


def draw_text(text, size, x, y):
    font_name = pygame.font.match_font("arial")
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, consts.BLACK)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    screen.blit(text_surface, text_rect)


def show_title_page():
    screen.fill(consts.WHITE)
    draw_text("Catch Earth", 70, consts.WINDOW_WIDTH / 2, consts.WINDOW_HEIGHT / 4)
    draw_text("Collect the earth icons while avoiding the polluting factories.", 30, consts.WINDOW_WIDTH / 2,
              consts.WINDOW_HEIGHT / 2.5)
    draw_text(f"Collect {consts.SCORE_TO_WIN} points in order to win", 30, consts.WINDOW_WIDTH / 2,
              consts.WINDOW_HEIGHT / 2.25)
    draw_text("Press any key to begin.", 30, consts.WINDOW_WIDTH / 2, consts.WINDOW_HEIGHT / 2)
    pygame.display.update()


def draw_game_over(msg):
    screen.fill(consts.WHITE)
    font = pygame.font.SysFont(consts.FONT_NAME, consts.FONT_SIZE)
    txt_image = font.render(msg, True, consts.BLACK)
    txt_rect = txt_image.get_rect()
    txt_rect.center = (consts.WINDOW_WIDTH // 2, consts.WINDOW_HEIGHT // 2)
    screen.blit(txt_image, txt_rect)
    pygame.display.update()
