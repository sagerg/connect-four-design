import pygame
from pygame.surface import Surface
from enums import Board, GUI
from connect_four_logic import ConnectFour


""" Function to render board after every move
"""
def draw_board(board: ConnectFour, radius: int, height: int, screen: Surface):
    board = board.board
    for r in range(len(board)):
        for c in range(len(board[0])):
            pygame.draw.rect(screen, GUI.BLUE.value, (c*GUI.SQUARESIZE.value, r*GUI.SQUARESIZE.value+GUI.SQUARESIZE.value, GUI.SQUARESIZE.value, GUI.SQUARESIZE.value))
            pygame.draw.circle(screen, GUI.BLACK.value, (int(c*GUI.SQUARESIZE.value+GUI.SQUARESIZE.value/2), int(r*GUI.SQUARESIZE.value+GUI.SQUARESIZE.value+GUI.SQUARESIZE.value/2)), radius)
     
    for r in range(len(board)):
        for c in range(len(board[0])):    
            if board[r][c] == 1:
                pygame.draw.circle(screen, GUI.RED.value, (int(c*GUI.SQUARESIZE.value+GUI.SQUARESIZE.value/2), int((r+1)* GUI.SQUARESIZE.value+GUI.SQUARESIZE.value/2)), radius)
            elif board[r][c] == 2: 
                pygame.draw.circle(screen, GUI.YELLOW.value, (int(c*GUI.SQUARESIZE.value+GUI.SQUARESIZE.value/2), int((r+1)*GUI.SQUARESIZE.value+GUI.SQUARESIZE.value/2)), radius)
    
    pygame.display.update()