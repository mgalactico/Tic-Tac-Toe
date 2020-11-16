MOVES = 0

def print_game(board):
    i = 0
    values = []
    print('---------')
    # create list of values from dictionary
    for value in board.values():
        values.append(value)

    # walk through list created above to print board
    while i < len(values):
        k = 0
        print('| ', end='')
        while k < 3:
            print(values[i], end=' ')
            i += 1
            k += 1
        print('|')
    print('---------')


def x_wins(_list):
    win = 0
    if ['X', 'X', 'X'] in _list:
        win += 1
    if _list[0][0] == _list[1][1] == _list[2][2] =='X':
        win += 1
    if _list[0][2] == _list[1][1] == _list[2][0] =='X':
        win += 1
    if _list[0][0] == _list[1][0] == _list[2][0] =='X':
        win += 1
    if _list[0][1] == _list[1][1] == _list[2][1] =='X':
        win += 1
    if _list[0][2] == _list[1][2] == _list[2][2] =='X':
        win += 1
    return win


def o_wins(_list):
    win = 0
    if ['O', 'O', 'O'] in _list:
        win += 1
    if _list[0][0] == _list[1][1] == _list[2][2] =='O':
        win += 1
    if _list[0][2] == _list[1][1] == _list[2][0] =='O':
        win += 1
    if _list[0][0] == _list[1][0] == _list[2][0] =='O':
        win += 1
    if _list[0][1] == _list[1][1] == _list[2][1] =='O':
        win += 1
    if _list[0][2] == _list[1][2] == _list[2][2] =='O':
        win += 1
    return win


def make_matrix(x):
    return [x[i:i+3] for i in range(0, len(x), 3)]


def evaluate_move(move, board):
    global MOVES
    clean_move = move.replace(' ', '')
    if not clean_move.isdigit():
        print('You should enter numbers!')
        return False
    elif move not in board:
        print('Coordinates should be from 1 to 3!')
        return False
    elif board[move] != ' ':
        print('This cell is occupied! Choose another one!')
        return False
    elif MOVES % 2 != 1 or MOVES == 0:
        board[move] = 'X'
        MOVES += 1
        return True
    else:
        board[move] = 'O'
        MOVES += 1
        return True


def determine_winner(board):
    answer = False
    while answer == False:
        move = input('Enter the coordinates: ')
        answer = evaluate_move(move, board)
    moves_list = []
    for value in board.values():
        moves_list.append(value)
    _list = make_matrix(moves_list)
    wins_by_x = x_wins(_list)
    wins_by_o = o_wins(_list)
    print_game(board)
    if  (wins_by_x == 1):
        print('X wins')
        return 'win'
    elif (wins_by_o == 1):
        print('O wins')
        return 'win'

board = {'1 3': ' ',  '2 3': ' ', '3 3': ' ', '1 2': ' ', '2 2': ' ', '3 2': ' ', '1 1': ' ', '2 1': ' ', '3 1': ' ',}
print_game(board)
win = ''
while (win != 'win') and (MOVES != 9):
    win = determine_winner(board)
    if (MOVES == 9) or (win != ''):
        print('Draw')
