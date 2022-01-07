class ConnectFour:

    def __init__(self):
        self.board = [[0 for y in range(7)] for x in range(6)]
        self.winner = 0
    
    def drop(self, pos, player):
        if self.winner > 0:
            print('winner:',self.winner) # cannot play game if there is already a winner
            return 1
        print('Player', player, 'is dropping at', pos)
        for row in range(len(self.board)-1,-1,-1):
            if self.board[row][pos] == 0:
                self.board[row][pos] = player
                if self.checkCol(player, (row,pos)) or\
                    self.checkRow(player, (row,pos)) or\
                    self.checkDiag(player, (row,pos)) or\
                    self.checkAntiDiag(player, (row,pos)):
                        self.winner = player
                        print('winner:', player)
                        return 0
                return 0
        return 1

    def checkCol(self, player, pos):
        row, col = pos
        values = []
        for r in range(len(self.board)):
            if self.board[r][col] == player:
                values.append(self.board[r][col])
        return len(values) == 4

    def checkRow(self, player, pos):
        row, col = pos
        values = []
        for c in range(len(self.board[0])):
            if self.board[row][c] == player:
                values.append(self.board[row][c])
        return len(values) == 4

    def checkDiag(self, player, pos):
        # topDiag goes up rightward: (x+1,y+1)
        # botDiag goes down leftward: (x-1,y-1)
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

    def checkAntiDiag(self, player, pos):
        # topDiag goes up leftward: (x+1,y-1)
        # botDiag goes down rightward: (x-1,y+1)
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
    
    def printBoard(self):
        if not self.board:
            return 1
        for i in range(len(self.board)):
            for j in range(len(self.board[0])):
                print(self.board[i][j], end =' ')
            print()
        print()
        return 0

# test

cf = ConnectFour()
PLAYER1 = 1
PLAYER2 = 2
# pos can be in range(0,8) : there are 7 columns 0-indexed
cf.drop(3,PLAYER1) # p1 drops at col=3
cf.printBoard()
cf.drop(3,PLAYER2) # p2 drops at col=3
cf.printBoard()
cf.drop(3,PLAYER1) # p1 drops at col=3
cf.printBoard()
cf.drop(2,PLAYER2) # p2 drops at col=2
cf.printBoard()
cf.drop(1,PLAYER2) # p2 drops at col=1
cf.printBoard()
cf.drop(0,PLAYER2) # p2 drops at col=0
cf.printBoard()
cf.drop(2,PLAYER2) # p2 drops at col=2
cf.printBoard()
cf.drop(1,PLAYER2) # p2 drops at col=1
cf.printBoard()
'''
TEST FOR ROW CHECK
cf.drop(0,PLAYER2) # p2 drops at col=0
cf.printBoard()
cf.drop(4,PLAYER1) # p1 drops at col=4 NOTE: there should be a winner already
cf.printBoard()'''


'''
TEST FOR COL CHECK
cf.drop(2,PLAYER2) # p2 drops at col=2
cf.printBoard()
cf.drop(2,PLAYER2) # p2 drops at col=2
cf.printBoard()'''

'''
TEST FOR DIAG CHECK
cf.drop(2,PLAYER2) # p2 drops at col=2
cf.printBoard()
cf.drop(3,PLAYER2) # p2 drops at col=2
cf.printBoard()'''
