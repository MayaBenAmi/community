import pygame
import time
import soldier_flag as soldier
import consts_flag as consts
import game_field_flag as game_field
import screen_flag as screen

soldier_x = 0
soldier_y = 0

def init_board():
    game_field.build_board()
    game_field.add_flag()
    game_field.add_mines()
    game_field.add_grass()


def main():
    global soldier_x
    global soldier_y

    pygame.init()
    init_board()

    game_over = False
    show_mines = False
    explode = False
    win = False
    dx = 0
    dy = 0
    while not game_over:
        # handle user events
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            elif event.type == pygame.KEYDOWN and not explode:
                if event.key == pygame.K_ESCAPE:
                    game_over = True
                elif event.key == pygame.K_DOWN:
                    dy = 1
                    soldier_y += dy
                elif event.key == pygame.K_UP:
                    dy = 1
                    soldier_y -= dy
                elif event.key == pygame.K_LEFT:
                    dx = 1
                    soldier_x -= dx
                elif event.key == pygame.K_RIGHT:
                    dx = 1
                    soldier_x += dx
                # if the user presses "enter" he can see the mines for the first second after pressing
                elif event.key == pygame.K_RETURN:
                    show_mines = True
                    start_show = time.time()
        if show_mines and time.time() > start_show + 1:
            show_mines = False

        # making sure that the soldier stays on the board
        if soldier_x < 0:
            soldier_x = 0
        elif soldier_x > consts.COL_NUM - consts.TURTLE_SIZE[0]:
            soldier_x = consts.COL_NUM - consts.TURTLE_SIZE[0]

        if soldier_y < 0:
            soldier_y = 0
        elif soldier_y > consts.ROW_NUM - consts.TURTLE_SIZE[1]:
            soldier_y = consts.ROW_NUM - consts.TURTLE_SIZE[1]

        # if solider explodes: display the screen announcing he lost for 3 seconds before shutting down the game
        # 'if not explode': so that the user wouldn't move after dying
        if not explode and soldier.turtle_on_plastic_bag(soldier_x, soldier_y):
            explode = True
            explosion_time = time.time()
        if explode and time.time() > explosion_time + 3:
            game_over = True

        screen.draw_game(game_field.board, (soldier_y, soldier_x), show_mines, explode)
        if explode:
            screen.draw_game_over('You Lost!')
        # if soldier gets to flag : display the screen announcing he won for 3 seconds before shutting down the game
        if not win and soldier.turtle_on_seaweed(soldier_x, soldier_y):
            win = True
            victory_time = time.time()

        if win and time.time() > victory_time + 3:
            game_over = True

        if win:
            screen.draw_game_over('You won!')

        pygame.display.flip()


if __name__ == '__main__':
    main()

