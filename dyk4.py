def open_dyk4():
    import pygame
    pygame.init()

    SIZE = WIDTH, HEIGHT = (500, 500)
    FPS = 50
    BLACK = (225, 225, 225)
    PINK = (30, 86, 49)

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

    TEXT = "Recycling helps our planet and our economy! \nIf all 37.4 million tons of recyclable materials from households were recycled each year, \nit would reduce greenhouse gas emissions equal to removing 20 million cars from U.S. highways" \
           "and support the creation of 370,000 jobs. \nWe can see that we all have to be persistent. \nTell a friend today how important it is to recycle."

    FONT = pygame.font.SysFont('Arial', 30)

    done = False
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                quit()
            if event.type == pygame.KEYDOWN:
                done = True

        screen.fill(PINK)
        pygame.display.set_caption("INSTRUCTIONS")
        blit_text(screen, TEXT, (20, 20), FONT)
        pygame.display.update()
