""" Hardcoded global values go here
"""


from enum import Enum


class Player(Enum):
    RED = 1
    YELLOW = 2


class Board(Enum):
    ROW = 6
    COL = 7


class GUI(Enum):
    SQUARESIZE = 100
    BLUE = (0,0,255)
    BLACK = (0,0,0)
    RED = (255,0,0)
    YELLOW = (255,255,0)