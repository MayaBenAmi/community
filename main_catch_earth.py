def catch_earth():
    import pygame
    import consts_catch_earth as consts
    import screen_catch_earth as screen
    import sys
    import player_catch_earth as player
    import random
    from pygame.locals import QUIT


    player_group = pygame.sprite.Group()
    player_group.add(player.my_player)
    all_sprites_list = pygame.sprite.Group()
    player.points = pygame.sprite.Group()
    player.attack_bubbles = pygame.sprite.Group()
    player.prizes = pygame.sprite.Group()
    clock = pygame.time.Clock()


    class Point(pygame.sprite.Sprite):
        def __init__(self):
            super(Point, self).__init__()
            self.image = pygame.image.load('earth_icon.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randint((0 + self.rect.width), (consts.WINDOW_WIDTH - self.rect.width))
            self.rect.y = random.randint((0 + self.rect.height), (consts.WINDOW_HEIGHT - self.rect.height))


    class Prize(pygame.sprite.Sprite):
        def __init__(self):
            super(Prize, self).__init__()
            self.image = pygame.image.load("turkish.png").convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randint((0 + self.rect.width), (consts.WINDOW_WIDTH - self.rect.width))
            self.rect.y = random.randint((0 + self.rect.height), (consts.WINDOW_HEIGHT - self.rect.height))


    class Attack(pygame.sprite.Sprite):
        def __init__(self):
            super(Attack, self).__init__()
            self.image = pygame.image.load('polluting_factory.png').convert_alpha()
            self.rect = self.image.get_rect()
            self.rect.x = random.randint((0 + self.rect.width), (consts.WINDOW_WIDTH - self.rect.width))
            self.rect.y = random.randint((0 + self.rect.height), (consts.WINDOW_HEIGHT - self.rect.height))
            self.speed_x = random.randint(1, 2)
            self.speed_y = random.randint(1, 2)

        def update(self):
            self.rect.x += self.speed_x
            self.rect.y += self.speed_y

            # Check collision with wall
            if (self.rect.left + self.speed_x) <= 0 or (self.rect.right + self.speed_x) >= consts.WINDOW_WIDTH:
                self.speed_x = -self.speed_x
            if (self.rect.top + self.speed_y) <= 0 or (self.rect.bottom + self.speed_y) >= consts.WINDOW_HEIGHT:
                self.speed_y = -self.speed_y


    def wait_for_start():
        done = False
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True
                if event.type == pygame.KEYDOWN:
                    done = True


    def main():
        pygame.init()
        pygame.mixer.init()
        player.init()
        screen.screen_init()
        screen.show_title_page()
        wait_for_start()

        sound = pygame.mixer.Sound("catchearth.mp3")
        game_over = False

        while not game_over:
            sound.play()
            while len(player.points) < 3:
                point = Point()
                all_sprites_list.add(point)
                player.points.add(point)
            while len(player.attack_bubbles) < 3:
                attack = Attack()
                all_sprites_list.add(attack)
                player.attack_bubbles.add(attack)

            if player.score < 0:
                sound.stop()
                screen.draw_game_over('You lost !!!')
                game_over = True

            if player.score == consts.SCORE_TO_WIN:
                sound.stop()
                screen.draw_game_over('You won !!!')
                game_over = True

            # Event Handling
            for event in pygame.event.get():
                if event.type == QUIT:
                    sound.stop()
                    pygame.quit()
                    sys.exit()
                if pygame.key.get_pressed():
                    player.handle_input(event)

            # Game display
            if not game_over:
                player_group.update()
                all_sprites_list.update()
                player.check_collision(player.points)
                player.check_collision(player.attack_bubbles)
                player.check_collision(player.prizes)
                screen.screen.fill(consts.WHITE)
                player_group.draw(screen.screen)
                all_sprites_list.draw(screen.screen)
                screen.draw_text("Current score is %d" % player.score, 18, consts.WINDOW_WIDTH / 2, 10)
                pygame.display.update()
                clock.tick(60)

        wait_for_start()

    main()
