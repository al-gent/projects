import random
class Board:
    """Represents a game board."""
    def __init__(self, h=6, w=7, c=4):
        self.h = h
        self.w = w
        self.c = c
        self.board = [[i+(w*j)+1 for i in range(w)] for j in range(h)]
        board = self.board
        self.diags = [board[i][i] for i in range(h)], [board[i][-i-1] for i in range(h)]
        self.corners = [board[0][0], board[0][-1], board[-1][0], board[-1][-1]]
        self.center = [[item for item in row if item != row[0] and item !=row[w-1]] for row in board if row!= board[0] and row!=board[h-1]]
        self.choices = [i for row in board for i in row if type(i) == int]

    def update(self, num, player):
        """takes an int and updates gameboard with the players choice"""
        x,y = self.num_to_coord(num)
        print(num)
        self.board[x][y] = player
        self.choices = [i for row in self.board for i in row if type(i) == int]

    def render(self):
        for row in self.board:
            print(row)
            
    def good_input(self, num):
        """Return True if x is an open position on the game board"""
        return num in self.choices
            
    def num_to_coord(self, num):
        return num // self.h, (num% self.w)
    
    def get_human_choice(self, player):
        """Recieve number coordinate from player
        returns number coordinate"""
        num = input(player + " is up. Enter board position: ")
        num = int(num)
        if self.good_input(num):
            return num -1
        else:
            print("Invalid input: try again")
            self.get_human_choice(player)

class Game:
    """ Takes Board object as input.
    Keeps score, checks for wins & draws, runs computer player"""
    def __init__(self, board):
        self.board = board
        
        
    def go(self, player, symbol):
        """One turn of the Game. Accepts player and symbol as argument
        renders board, updates board, checks for win or draw
        """
        
        b = self.board
        b.render()
        if player == 'H':
            num = b.get_human_choice(symbol)
        if player == 'random':
            num = Opponent(b).random()-1
        b.update(num, symbol)

     
    def play(self, p1='random', p2='H'):
        """ Accepts Humans('H'), or CPUs('random')('smart') as P1, P2
        Run the play sequence, take turns, check for winners, check for draws"""
        b = self.board
        while True:
            self.go(p1, 'X')
            if self.check_win():
                print('X wins!')
                b.render()
                break
            if self.check_cats():
                print('Cats Game')
                break
            self.go(p2, 'O')
            if self.check_win():
                print('O wins!')
                b.render()
                break
            if self.check_cats():
                print('Cats Game')
                break
            
        
    def check_win(self):
        """Return True if a player has won"""
        board = self.board.board
        #win across
        for row in board:
            if row[0] == row[1] == row[2]:
                return True
        #win up/down
        cols = [[row[i] for row in board] for i in range(3)]
        for col in cols:
            if col[0] == col[1] == col[2]:
                return True
        #win diag
        diags = [[board[0][0], board[1][1], board[2][2]], [board[2][0],board[1][1],board[0][2]]]
        for diag in diags:
            if diag[0] == diag[1] == diag[2]:
                return True

    def check_cats(self):
        """Return True if the game is draw"""
        board = self.board.board
        cats_count = 7
        for row in board:
            if "X" in row and "O" in row:
                cats_count -= 1
        cols = [[row[i] for row in board] for i in range(3)]
        for col in cols:
            if "X" in col and "O" in col:
                cats_count -= 1
        diags = [[board[0][0], board[1][1], board[2][2]], [board[2][0],board[1][1],board[0][2]]]
        for diag in diags:
            if "X" in diag and "O" in diag:
                cats_count -= 1
        return cats_count == 0

class Opponent:
    """A computer opponent"""
    def __init__(self, board):
        self.Board = board
        
    def random(self):
        return random.choice(self.Board.choices)
    
    def smart(self):
        
    


g = Game(Board(4,4))

g.play('random','random')
