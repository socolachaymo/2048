import random 
def start_game():
    board = []
    for _ in range(4):
        board.append([0]*4)
    board = add_new_number(board)
    return board
def add_new_number(board):
    r = random.randint(0,3)
    c = random.randint(0,3)
    while board[r][c] != 0:
        r = random.randint(0,3)
        c = random.randint(0,3)
    if random.random() < 0.9:
        board[r][c] = 2
    else:
        board[r][c] = 4
    return board
def current_state(board):
    for i in range(4):
        for j in range(4):
            if board[i][j] == 2048:
                print(i,j,board[i][j])
                return 'Congratulations!'
    for i in range(4):
        for j in range(4):
            if board[i][j] == 0:
                return 'Continue'
    for i in range(3):
        for j in range(3):
            if board[i][j] == board[i][j+1] or board[i][j] == board[i+1][j]:
                return 'Continue'
    for i in range(3):
        if board[i][3] == board[i+1][3]:
            return 'Continue'
    for j in range(3):
        if board[3][j] == board[3][j+1]:
            return 'Continue'
    return 'Game over'
def compress(board):
    new_board = []
    changed = False
    for _ in range(4):
        new_board.append([0]*4)
    for i in range(4):
        pos = 0
        for j in range(4):
            if board[i][j] != 0:
                new_board[i][pos] = board[i][j]
                if j != pos:
                    changed = True
                pos += 1
    return new_board, changed
def merge(board):
    changed = False
    for i in range(4):
        for j in range(3):
            if board[i][j] == board[i][j+1] and board[i][j] != 0:
                board[i][j] = board[i][j]*2
                board[i][j+1] = 0
                changed = True
    return board, changed
def reverse(board):
    new_board = []
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[i][3-j])
    return new_board
def transpose(board):
    new_board = []
    for i in range(4):
        new_board.append([])
        for j in range(4):
            new_board[i].append(board[j][i])
    return new_board
def move_left(board):
    board, changed1 = compress(board)
    board, changed2 = merge(board)
    changed = changed1 or changed2
    board, _ = compress(board)
    return board, changed
def move_right(board):
    board = reverse(board)
    board, changed = move_left(board)
    board = reverse(board)
    return board, changed
def move_up(board):
    board = transpose(board)
    board, changed = move_left(board)
    board = transpose(board)
    return board, changed
def move_down(board):
    board = transpose(board)
    board, changed = move_right(board)
    board = transpose(board)
    return board, changed
