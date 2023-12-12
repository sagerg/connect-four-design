from enums import Player, Board


""" Connect four class
"""
class ConnectFour:  
    def __init__(self, board = [[0 for y in range(Board.COL.value)] for x in range(Board.ROW.value)], winner = 0):
        self.board = board
        self.winner = winner


    def __str__(self) -> None:
        if not self.board:
            return ''
        str_builder = ''
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                str_builder += str(self.board[i][j]) + ' '
            str_builder += '\n'
        str_builder += 'Winner: ' + ('None' if not self.__is_there_a_winner() else str(Player(self.winner).name) + ', ' + str(self.winner))
        str_builder += '\n'
        return str_builder


    """ Check if move is valid and drop player's circle in board
    """
    def drop(self, at_column: int, player: int) -> tuple:
        if not self.__is_there_a_winner():
            for row in range(len(self.board) - 1, -1, -1):
                if self.board[row][at_column] == 0:

                    # Drop player's circle in this column
                    self.board[row][at_column] = player

                    if self.is_game_over(player, row, at_column):
                        self.winner = player

                        return (True, player)
                    
                    # Exit out of loop once we've found a valid move
                    else:
                        return (True, 0)

            # Exit out of loop if there are no valid moves in this column
            return (False, 0)
        
        else:
            return (False, self.winner)


    """ Check if game session is over
    """
    def is_game_over(self, player: int, row: int, col: int) -> bool:
        return (
            self.__is_column_won(player, (row, col))\
            or self.__is_row_won(player, (row, col))\
            or self.__is_diag_won(player, (row, col))\
            or self.__is_anti_diag_won(player, (row, col))
        )


    """ Check if there is a winner
    """
    def __is_there_a_winner(self) -> bool:
        return self.winner in [Player.RED.value, Player.YELLOW.value]


    """ Check | direction for winners
    """
    def __is_column_won(self, player, pos) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]
                except IndexError:
                    return False


    """ Check -- direction for winners
    """
    def __is_row_won(self, player, pos) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]
                except IndexError:
                    return False


    """ Check / direction for winners
    """
    def __is_diag_won(self, player, pos) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]
                except IndexError:
                    return False


    """ Check \ direction for winners
    """
    def __is_anti_diag_won(self, player, pos) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]
                except IndexError:
                    return False
