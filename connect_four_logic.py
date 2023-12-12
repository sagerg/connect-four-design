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
    

    def __deepcopy__(self, memo):
        board_copy = [[y for y in range(Board.COL.value)] for i in range(len(self.board))]
        winner_copy = self.winner
        return ConnectFour(board=board_copy, winner=winner_copy)


    """ Check if move is valid and drop player's circle in board
        Return values can be:
            True, 1 | 2     - Move is valid and there is a winner
            True, 0         - Move is valid and there is no winner, game continues
            False, 1 | 2    - Move is not valid and there is no winner
            False, 0        - There is already a winner (move automatically not valid)
    """
    def drop(self, at_column: int, player: int) -> tuple:
        if not self.__is_there_a_winner():
            for row in range(len(self.board) - 1, -1, -1):
                if self.board[row][at_column] == 0:

                    # Drop player's circle in this column
                    self.board[row][at_column] = player

                    if self.is_game_over(player):
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
    def is_game_over(self, player: int) -> bool:
        return (
            self.__is_column_won(player) \
            or self.__is_row_won(player) \
            or self.__is_diag_won(player) \
            or self.__is_anti_diag_won(player)
        )


    """ Check if there is a winner
    """
    def __is_there_a_winner(self) -> bool:
        return self.winner in [Player.RED.value, Player.YELLOW.value]


    """ Check | direction for winners
    """
    def __is_column_won(self, player) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i][j+1] == self.board[i][j+2] == self.board[i][j+3]
                except IndexError:
                    continue
        return False


    """ Check -- direction for winners
    """
    def __is_row_won(self, player) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i+1][j] == self.board[i+2][j] == self.board[i+3][j]
                except IndexError:
                    continue
        return False


    """ Check / direction for winners
    """
    def __is_diag_won(self, player) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i+1][j+1] == self.board[i+2][j+2] == self.board[i+3][j+3]
                except IndexError:
                    continue
        return False


    """ Check \ direction for winners
    """
    def __is_anti_diag_won(self, player) -> bool:
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                try:
                    if player == self.board[i][j]:
                        return self.board[i][j] == self.board[i+1][j-1] == self.board[i+2][j-2] == self.board[i+3][j-3]
                except IndexError:
                    continue
        return False
