import pytest
from src.enums import Player
from src.managers.connect_four_manager import ConnectFour


@pytest.fixture
def connect_four_game_1():
    red = Player.RED.value
    yellow = Player.YELLOW.value
    cf = ConnectFour()
    
    moves = [
        (0, red),(1, yellow),(0, red),(1, yellow),
        (0, red),(1, yellow),(0, red),(1, yellow),
    ]
    response = {}
    for move in moves:
        column, player = move
        response = cf.drop(at_column=column, player=player)
    
    return response.winner # RED WINS


@pytest.fixture
def connect_four_game_2():
    red = Player.RED.value
    yellow = Player.YELLOW.value
    cf = ConnectFour()

    moves = [
        (0, red),(1, yellow),(2, red),(2, yellow),
        (3, red),(0, yellow),(3, red),(3, yellow),
        (4, red),(4, yellow),(4, red),(4, yellow),
    ]
    response = {}
    for move in moves:
        column, player = move
        response = cf.drop(at_column=column, player=player)
    
    return response.winner # YELLOW WINS


def test_connect_four_game_red(connect_four_game_1):
    # Act
    result = connect_four_game_1

    # Assert
    assert result == Player.RED.value


def test_connect_four_game_yellow(connect_four_game_2):
    # Act
    result = connect_four_game_2

    # Assert
    assert result == Player.YELLOW.value
