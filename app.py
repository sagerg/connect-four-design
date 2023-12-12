import sys
import math
import random
import pygame
from connect_four_logic import ConnectFour
from minimax import minimax
from enums import Player, Board, GUI
from utils import draw_board


""" Setup and manage game session
"""
def app():

    # Instantiate ConnectFour game
    board = ConnectFour()
    game_over = False
    
    # Start game
    pygame.init()

    radius = int(GUI.SQUARESIZE.value/2 - 5)
    width = Board.COL.value * GUI.SQUARESIZE.value
    height = (Board.ROW.value+1) * GUI.SQUARESIZE.value
    size = (width, height)
    screen = pygame.display.set_mode(size)

    # Render board
    draw_board(board, radius, height, screen)

    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    red = Player.RED.value
    yellow = Player.YELLOW.value

    turn = red

    while not game_over:
        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, GUI.BLACK.value, (0,0, width, GUI.SQUARESIZE.value))
                posx = event.pos[0]
                if turn == red:
                    pygame.draw.circle(screen, GUI.RED.value, (posx, int(GUI.SQUARESIZE.value/2)), radius)
            
            # Rerender board
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, GUI.BLACK.value, (0, 0, width, GUI.SQUARESIZE.value))

                # When red has to move
                if turn == red:
                    posx = event.pos[0]
                    col = int(math.floor(posx/GUI.SQUARESIZE.value))

                    is_move_valid, winner = board.drop(col, red)
                    has_won = winner in [Player.RED.value, Player.YELLOW.value]

                    if is_move_valid:
                        if has_won:
                            label = myfont.render("Red wins!", 1, GUI.RED.value)
                            screen.blit(label, (40,10))
                            game_over = True
                    
                        # Render board after a move has been made
                        draw_board(board, radius, height, screen)
                        print(board)

                        # Interchange turns between red and yellow
                        turn = red if turn == yellow else yellow

                    else:

                        # Game has already ended and there is a winner
                        if has_won:
                            label = myfont.render("Red wins!", 1, GUI.RED.value)
                            screen.blit(label, (40,10))
                            game_over = True

        # When yellow has to move which is the AI player
        if turn == yellow and not game_over:
            #col = random.randint(0, Board.COL.value-1)
            col, _ = minimax(board, 5, -math.inf, math.inf, True)

            if col is None:
                continue

            is_move_valid, winner = board.drop(col, yellow)
            has_won = winner in [Player.RED.value, Player.YELLOW.value]

            if is_move_valid:
                pygame.time.wait(500)
                if has_won:
                    label = myfont.render("Yellow wins!", 1, GUI.YELLOW.value)
                    screen.blit(label, (40,10))
                    game_over = True

                # Render board after a move has been made
                draw_board(board, radius, height, screen)
                print(board)

                # Interchange turns between red and yellow
                turn = red if turn == yellow else yellow

            else:

                # Game has already ended and there is a winner
                if has_won:
                    label = myfont.render("Yellow wins!", 1, GUI.YELLOW.value)
                    screen.blit(label, (40,10))
                    game_over = True

        # Let game wait before quitting
        if game_over:
            pygame.time.wait(3000)


if __name__ == "__main__":
    app()