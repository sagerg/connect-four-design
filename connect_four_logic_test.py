import pytest
from enums import Player
from connect_four_logic import ConnectFour


@pytest.fixture(scope='function', autouse=True)
def connect_four_game_1():
    red = Player.RED.value
    yellow = Player.YELLOW.value
    cf = ConnectFour()
    
    moves = [
        (0, red),(1, yellow),(0, red),(1, yellow),
        (0, red),(1, yellow),(0, red),(1, yellow),
    ]

    for move in moves:
        column, player = move
        _, winner = cf.drop(at_column=column, player=player)
    print(cf)
    return winner # RED WINS


@pytest.fixture(scope='function', autouse=True)
def connect_four_game_2():
    red = Player.RED.value
    yellow = Player.YELLOW.value
    cf = ConnectFour()

    moves = [
        (0, red),(1, yellow),(2, red),(2, yellow),
        (3, red),(0, yellow),(3, red),(3, yellow),
        (4, red),(4, yellow),(4, red),(4, yellow),
    ]

    for move in moves:
        column, player = move
        _, winner = cf.drop(at_column=column, player=player)
    print(cf)
    return winner # YELLOW WINS


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
