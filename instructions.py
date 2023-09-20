import pygame

pygame.init()

SIZE = WIDTH, HEIGHT = (500, 500)
FPS = 50
BLACK = (0, 0, 0)
PINK = (255, 228, 225)

screen = pygame.display.set_mode(SIZE)


def blit_text(surface, text, pos, font, color=BLACK):
    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]  # The width of a space.
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]  # Reset the x.
                y += word_height  # Start on new row.
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]  # Reset the x.
        y += word_height  # Start on new row.


TEXT = "Welcome to the game!\nYour task in the game is to keep the bunny happy, by raising awareness about protecting the environment.\n" \
       "As long as you play at least one game in a 24-hour span, your rabbit will remain happy! \nGOOD LUCK!"

FONT = pygame.font.SysFont('Arial', 30)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            quit()
    screen.fill(PINK)
    pygame.display.set_caption("INSTRUCTIONS")
    blit_text(screen, TEXT, (20, 20), FONT)
    pygame.display.update()
