board = [[None for _ in range(3)] for _ in range(3)]
for row in board:
    print(row)

def next_turn(player):
    x,y = input(player+ " is up: enter coordinates: ").split(",")
    x=int(x)
    y=int(y)
    if x > 2 or y > 2 or board[y][x] is not None:
        print("Invalid move")
        return next_turn(player)
    board[y][x] = str(player)
    for row in board:
        print(row)
        

def check_win():
    #win across
    for row in board:
        if None not in row and row[0] == row[1] == row[2]:
            print('winner! Across')
            return True
    #win up/down
    cols = [[row[i] for row in board] for i in range(3)]
    for col in cols:
        if None not in col and col[0] == col[1] == col[2]:
            print('winner! Up/Down')
            return True
    #win diag
    diags = [[board[0][0], board[1][1], board[2][2]], [board[2][0],board[1][1],board[0][2]]]
    for diag in diags:
        if None not in diag and diag[0] == diag[1] == diag[2]:
            print('winner! Diagonal')
            return True
        
def play():
    while True:
        next_turn("X")
        if check_win():
            break
        next_turn("O")
        if check_win():
            break
        
play()
