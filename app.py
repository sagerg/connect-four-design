import sys
import math
import pygame
from connect_four_logic import ConnectFour
from enums import Player, Board, GUI
from utils import draw_board


def app():
    board = ConnectFour()
    game_over = False
    turn = 0
    pygame.init()
    radius = int(GUI.SQUARESIZE.value/2 - 5)
    width = Board.COL.value * GUI.SQUARESIZE.value
    height = (Board.ROW.value+1) * GUI.SQUARESIZE.value
    size = (width, height)
    screen = pygame.display.set_mode(size)
    draw_board(board, radius, height, screen)
    pygame.display.update()

    myfont = pygame.font.SysFont("monospace", 75)

    red = Player.RED.value
    yellow = Player.YELLOW.value

    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

            if event.type == pygame.MOUSEMOTION:
                pygame.draw.rect(screen, GUI.BLACK.value, (0,0, width, GUI.SQUARESIZE.value))
                posx = event.pos[0]
                if turn == 0:
                    pygame.draw.circle(screen, GUI.RED.value, (posx, int(GUI.SQUARESIZE.value/2)), radius)
                else: 
                    pygame.draw.circle(screen, GUI.YELLOW.value, (posx, int(GUI.SQUARESIZE.value/2)), radius)
            pygame.display.update()

            if event.type == pygame.MOUSEBUTTONDOWN:
                pygame.draw.rect(screen, GUI.BLACK.value, (0, 0, width, GUI.SQUARESIZE.value))

                if turn == 0: # p1 turn
                    posx = event.pos[0]
                    col = int(math.floor(posx/GUI.SQUARESIZE.value))

                    status, winner = board.drop(col, red)
                    has_won = winner in [Player.RED.value, Player.YELLOW.value]
                    if not status and not has_won:
                        continue
                    elif status and has_won:
                        label = myfont.render("Player Red wins!", 1, GUI.RED.value)
                        screen.blit(label, (40,10))
                        game_over = True
                else:
                    posx = event.pos[0]
                    col = int(math.floor(posx/GUI.SQUARESIZE.value))

                    status, winner = board.drop(col, yellow)
                    has_won = winner in [Player.RED.value, Player.YELLOW.value]
                    if not status and not has_won:
                        continue
                    elif status and has_won:
                        label = myfont.render("Player Yellow wins!", 1, GUI.RED.value)
                        screen.blit(label, (40,10))
                        game_over = True

                draw_board(board, radius, height, screen)

                turn += 1
                turn = turn % 2

                if game_over:
                    pygame.time.wait(3000)


if __name__ == "__main__":
    app()