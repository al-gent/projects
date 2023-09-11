import random

class Board:
    def __init__(self, h=3, w=3):
        self.h = h
        self.w = w
        self.board = [[1,2,3],[4,5,6],[7,8,9]]
        next_door = {1:[2,4], 2:[1,3,5], 3:[2,6], 4:[1,5,7], 5:[2,4,6,8], 6:[3,5,9], 7:[4,8], 8:[5,7,9], 9:[6,8]}
        #make flexible board size
        #self.board = [[i for i in range(w)] for _ in range(h)]
        self.choices = []
        for row in self.board:
            for i in row:
                if type(i) == int:
                    self.choices.append(i)
        self.side = [2,4,6,8]
        self.corners = [1,3,7,9]
        self.center = [5]
        
    def print_board(self):
        for row in self.board:
            print(row)
            
class Game_manager:
    def __init__(self, board, player):
        self.board = board
        self.player = player
        self.player2 = 'X' if player == 'O' else 'O'
        self.moves = []

    def good_input(x):
        if x not in '123456789':
            return False
        return 0 < int(x) < 10

    def num_to_coord(num):
        x = (num%3)-1
        if 0 < num < 4:
            y = 0
        elif 3 < num < 7:
            y = 1
        elif 6 < num < 10:
            y = 2
        return (x,y)


    def check_win(self):
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

    def check_cats():
        cats_count = 8
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
    
    def winning_move(board, player):
        for row in board:
            count = 0
            for i in row:
                if i == player:
                    count += 1
            if count == 2:
                for i in row:
                    if type(i) == int:
                        num = i
                        x,y = num_to_coord(num)
                        board[y][x] = player
                        break
        cols = [[row[i] for row in board] for i in range(3)]
        for col in cols:
            count = 0
            for i in col:
                if i == player:
                    count += 1
            if count == 2:
                for i in col:
                    if type(i) == int:
                        num = i
                        x,y = num_to_coord(num)
                        board[y][x] = player
                        break
        diags = [[board[0][0], board[1][1], board[2][2]], [board[2][0],board[1][1],board[0][2]]]
        for diag in diags:
            count = 0
            for i in diag:
                if i == player:
                    count += 1
            if count == 2:
                for i in diag:
                    if type(i) == int:
                        num = i
                        x,y = num_to_coord(num)
                        board[y][x] = player
                        break

class Human:
    def __init__(self):
        pass
    def go(board, player):
        num = input(player+ " is up. Enter board position: ")
        if good_input(num):
            num = int(num)
        else:
            print("Invalid input: try again")
            next_turn(player, board)
        x,y = num_to_coord(num)
        if type(board[y][x]) == str:
            print('Seats taken - lose a turn.')
            return 
        board[y][x] = str(player)
        return num

class Opponent:
    def __init__(self):
        self.board = Board()
        pass
    
    def go(board, player, moves):
        board = Board.board
        choices = []
        care = True
        for row in board:
            for i in row:
                if type(i) == int:
                    choices.append(i)
        side = [2,4,6,8]
        corners = [1,3,7,9]
        center = [5]
        #going first
        if len(choices) == 9:
            num = random.choice(side)
            x,y = num_to_coord(num)
            board[y][x] = player
            print('num:', num)
            return num
        if len(choices) == 7:
            if 5 in choices:
                num = 5
                return num
            else:
                num = random.choice(corners)
                care = False
                x,y = num_to_coord(num)
                board[y][x] = player
                return num
        if len(choices) == 5:
            if care:
                num = random.choice(next_door[moves[0]])
                x,y = num_to_coord(num)
                board[y][x] = player
                return num
            else:
                print('I dont care')
                num = random.choice(choices)
                x,y = num_to_coord(num)
                board[y][x] = player
                return num
        if len(choices) == 3:
            if care:
                winning_move(board, player)
                return num
                
            else:
                num = random.choice(choices)
                x,y = num_to_coord(num)
                board[y][x] = player
                return num
        if len(choices) == 1:
            num = random.choice(choices)
            x,y = num_to_coord(num)
            board[y][x] = player
            return num
            

def smart_play(board, player):
    moves =[]
    if player == 'X':
        player2 = 'O'
    else:
        player2 = 'X'
    while True:
        
        move = opponent.go(board, player, moves)
        moves.append(move)
        print('moves:',moves)
        for row in board:
            print(row) 
        if game_manager.check_win():
            for row in board:
                print(row) 
            print('You Lose! Loser!')
            break
        if game_manager.check_cats():
            print('Cats Game')
            break
        moves.append(human.go(board, player2))
        if game_manager.check_win():
            for row in board:
                print(row) 
            print('You win!')
            break
        if game_manager.check_cats():
            print('Cats Game')
            break


smart_play(Board.board, 'O')

