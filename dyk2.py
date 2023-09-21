def open_dyk2():
    import pygame
    pygame.init()

    SIZE = WIDTH, HEIGHT = (500, 500)
    FPS = 50
    BLACK = (225, 225, 225)
    PINK = (76, 154, 42)

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

    TEXT = "Cardboard boxes (like cereal boxes, for example) can be recycled at least seven \ntimes and can be used to make new packaging boxes and even furniture! \nThe best part is, recycling cardboard is easy. " \
           "Almost all Americans having access to curbside recycling for their corrugated boxes. \nJust make sure before you put them in the recycle bin that they’re \nempty, dry, clean, and flattened:)"

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
