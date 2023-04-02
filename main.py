import pygame

pygame.init()
# Setting caption for game window
pygame.display.set_caption("Tic Tac Toe")
# Height or width of the game window
width, height = 1000, 800
# Displaying the game window (we pass this in our main program)
window = pygame.display.set_mode((width, height))

# Set colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
green = (0, 255, 0)
window.fill(white)
# Frames per second
fps = 15
# Set in game font
font = pygame.font.SysFont("Arial", 32)

# B00 = pygame.draw.rect(window, black, (170, 65, 660, 670), 5)
C00 = pygame.draw.circle(window, white, (280, 180), 100, 2)
C01 = pygame.draw.circle(window, white, (500, 180), 100, 2)
C02 = pygame.draw.circle(window, white, (720, 180), 100, 2)
C10 = pygame.draw.circle(window, white, (280, 400), 100, 2)
C11 = pygame.draw.circle(window, white, (500, 400), 100, 2)
C12 = pygame.draw.circle(window, white, (720, 400), 100, 2)
C20 = pygame.draw.circle(window, white, (280, 620), 100, 2)
C21 = pygame.draw.circle(window, white, (500, 620), 100, 2)
C22 = pygame.draw.circle(window, white, (720, 620), 100, 2)
# Make playing area
HL1 = pygame.draw.line(window, black, (170, 290), (825, 290), 5)
HL2 = pygame.draw.line(window, black, (170, 510), (825, 510), 5)
VL1 = pygame.draw.line(window, black, (390, 65), (390, 730), 5)
VL2 = pygame.draw.line(window, black, (610, 65), (610, 730), 5)
playArea = [(C00, 0, 0), (C01, 0, 1), (C02, 0, 2), (C10, 1, 0), (C11, 1, 1), (C12, 1, 2), (C20, 2, 0), (C21, 2, 1),
            (C22, 2, 2)]
# Reset button
rst = pygame.draw.circle(window, green, (925, 400), 20, 20)
# Grid for console and backend checking
grid = [[None, None, None], [None, None, None], [None, None, None]]


def make_grid():
    pygame.draw.line(window, black, (170, 290), (825, 290), 5)
    pygame.draw.line(window, black, (170, 510), (825, 510), 5)
    pygame.draw.line(window, black, (390, 65), (390, 730), 5)
    pygame.draw.line(window, black, (610, 65), (610, 730), 5)
    pygame.draw.circle(window, green, (925, 400), 20, 20)


def check_win():
    # Row Win for X
    if grid[0][0] == 1 and grid[0][1] == 1 and grid[0][2] == 1:
        print("3 X in Row 1! X Wins!")
        display_msg("X", "row")
        return True
    elif grid[1][0] == 1 and grid[1][1] == 1 and grid[1][2] == 1:
        print("3 X in Row 2! X Wins!")
        display_msg("X", "row")
        return True
    elif grid[2][0] == 1 and grid[2][1] == 1 and grid[2][2] == 1:
        print("3 X in Row 3! X Wins!")
        display_msg("X", "row")
        return True
    # Column Win for X
    elif grid[0][0] == 1 and grid[1][0] == 1 and grid[2][0] == 1:
        print("3 X in Column 1! X Wins!")
        display_msg("X", "column")
        return True
    elif grid[0][1] == 1 and grid[1][1] == 1 and grid[2][1] == 1:
        print("3 X in Column 2! X Wins!")
        display_msg("X", "column")
        return True
    elif grid[0][2] == 1 and grid[1][2] == 1 and grid[2][2] == 1:
        print("3 X in Column 3! X Wins!")
        display_msg("X", "column")
        return True
    # Diagonal Win for X
    elif grid[0][0] == 1 and grid[1][1] == 1 and grid[2][2] == 1:
        print("3 X in Diagonal! X Wins!")
        display_msg("X", "diagonal")
        return True
    elif grid[0][2] == 1 and grid[1][1] == 1 and grid[2][0] == 1:
        print("3 X in Diagonal! X Wins!")
        display_msg("X", "diagonal")
        return True
    # Row Win for O
    elif grid[0][0] == 0 and grid[0][1] == 0 and grid[0][2] == 0:
        print("3 O in Row 1! O Wins!")
        display_msg("O", "row")
        return True
    elif grid[1][0] == 0 and grid[1][1] == 0 and grid[1][2] == 0:
        print("3 O in Row 2! O Wins!")
        display_msg("O", "row")
        return True
    elif grid[2][0] == 0 and grid[2][1] == 0 and grid[2][2] == 0:
        print("3 O in Row 3! O Wins!")
        display_msg("O", "row")
        return True
    # Column Win for O
    elif grid[0][0] == 0 and grid[1][0] == 0 and grid[2][0] == 0:
        print("3 O in Column 1! O Wins!")
        display_msg("O", "column")
        return True
    elif grid[0][1] == 0 and grid[1][1] == 0 and grid[2][1] == 0:
        print("3 O in Column 2! O Wins!")
        display_msg("O", "column")
        return True
    elif grid[0][2] == 0 and grid[1][2] == 0 and grid[2][2] == 0:
        print("3 O in Column 3! O Wins!")
        display_msg("O", "column")
        return True
    # Diagonal Win for O
    elif grid[0][0] == 0 and grid[1][1] == 0 and grid[2][2] == 0:
        print("3 O in Diagonal! O Wins!")
        display_msg("O", "diagonal")
        return True
    elif grid[0][2] == 0 and grid[1][1] == 0 and grid[2][0] == 0:
        print("3 O in Diagonal! O Wins!")
        display_msg("O", "diagonal")
        return True
    else:
        return False


def display_msg(winner, place):
    msg = winner + " wins! Three " + winner + " in a " + place + "!"
    win_message = font.render(msg, True, white, blue)
    msg_box = win_message.get_rect()
    msg_box.center = width // 2, height // 2
    window.blit(win_message, msg_box)
    print("Win message displayed!")


def display_draw_msg():
    msg = "Game Draw!"
    win_message = font.render(msg, True, white, blue)
    msg_box = win_message.get_rect()
    msg_box.center = width // 2, height // 2
    window.blit(win_message, msg_box)
    print("Draw message displayed!")


def set_xo(pos, who):
    game_stopped = False
    for co in playArea:
        if co[0].collidepoint(pos) and grid[co[1]][co[2]] is None:
            grid[co[1]][co[2]] = who
            draw_xo(who, co[0])
            game_stopped = check_win()
            return game_stopped, True
        elif rst.collidepoint(pos):
            reset_grid(pos)
        else:
            pass
    return False, False


def reset_grid(pos):
    if rst.collidepoint(pos):
        for i in range(3):
            for j in range(3):
                grid[i][j] = None
        window.fill(white)
        make_grid()
        print("Game was reset!")
    else:
        pass


def draw_xo(player, position):
    x, y = position[0], position[1]
    if player == 1:
        pygame.draw.line(window, blue, (x + 10, y + 10), (x + 190, y + 190), 20)
        pygame.draw.line(window, blue, (x + 190, y + 10), (x + 10, y + 190), 20)
    else:
        pygame.draw.circle(window, red, (x + 100, y + 100), 100, 20)


def main():
    play_count = 0
    turn = 1
    game_over = False
    game_draw = False
    clock = pygame.time.Clock()
    run = True
    while run:
        # With clock, the while loop runs only fps times per second otherwise it will be way faster
        clock.tick(fps)
        pygame.display.flip()
        # Check for events in the game
        for event in pygame.event.get():
            # curr_pos = pygame.mouse.get_pos()
            # First event to check is if the user wants to quit
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.MOUSEBUTTONUP and game_over is False:
                curr_pos = pygame.mouse.get_pos()
                game_over, flip_turn = set_xo(curr_pos, turn)
                if flip_turn is True:
                    play_count += 1
                    if turn == 1:
                        turn = 0
                    else:
                        turn = 1
            elif game_over is True:
                curr_pos = pygame.mouse.get_pos()
                reset_grid(curr_pos)
                turn = 1
                game_over = False
                play_count = 0
            elif game_over is False and play_count == 9 and game_draw is False:
                game_draw = True
                display_draw_msg()
                print("Game Draw!")


if __name__ == "__main__":
    main()
