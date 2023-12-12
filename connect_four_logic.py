from enums import Player, Board


class ConnectFour:
    def __new__(cls): 
        return super(ConnectFour, cls).__new__(cls) 
    
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
        str_builder += '\n'
        str_builder += 'Winner: ' + ('None' if not self.__is_there_a_winner() else str(Player(self.winner).name) + ', ' + str(self.winner))
        return str_builder
    

    def drop(self, at_column: int, player: int) -> dict:
        if not self.__is_there_a_winner():
            for row in range(len(self.board) - 1, -1, -1):
                if self.board[row][at_column] == 0:

                    # drop player chip in this column
                    self.board[row][at_column] = player

                    if self.is_game_over(player, row, at_column):
                        self.winner = player

                        return self
                    
                    # exit out of loop once we've found target cell
                    break
        else:
            return self


    def is_game_over(self, player: int, row: int, col: int) -> bool:
        return (
            self.__is_column_won(player, (row, col))\
            or self.__is_row_won(player, (row, col))\
            or self.__is_diag_won(player, (row, col))\
            or self.__is_anti_diag_won(player, (row, col))
        )


    def __is_there_a_winner(self) -> bool:
        return self.winner in [Player.RED.value, Player.YELLOW.value]


    def __is_column_won(self, player, pos) -> bool:
        _, col = pos
        values = []
        for row in range(len(self.board)):
            if self.board[row][col] == player:
                values.append(self.board[row][col])
        return len(values) == 4


    def __is_row_won(self, player, pos) -> bool:
        row, _ = pos
        values = []
        for col in range(len(self.board[0])):
            if self.board[row][col] == player:
                values.append(self.board[row][col])
        return len(values) == 4


    def __is_diag_won(self, player, pos) -> bool:

        # top diag goes up rightward: (x + 1, y + 1)
        # bot diag goes down leftward: (x - 1, y - 1)

        row, col = pos
        values = []
        while row in range(len(self.board)) and col in range(len(self.board[0])):
            if self.board[row][col] == player:
                values.append(player)
            row = row + 1
            col = col + 1
        row, col = pos
        row = row - 1
        col = col - 1
        while row in range(len(self.board)) and col in range(len(self.board[0])):
            if self.board[row][col] == player:
                values.append(player)
            row = row - 1
            col = col - 1
        return len(values) == 4


    def __is_anti_diag_won(self, player, pos) -> bool:

        # top diag goes up leftward: (x + 1, y - 1)
        # bot diag goes down rightward: (x - 1, y + 1)

        row, col = pos
        values = []
        while row in range(len(self.board)) and col in range(len(self.board[0])):
            if self.board[row][col] == player:
                values.append(player)
            row = row + 1
            col = col - 1
        row, col = pos
        row = row - 1
        col = col + 1
        while row in range(len(self.board)) and col in range(len(self.board[0])):
            if self.board[row][col] == player:
                values.append(player)
            row = row - 1
            col = col + 1
        return len(values) == 4
