print(" ----------------------\n Let's play Py-Pac-Poe!\n ----------------------")

board = {
    'a1': ' ',
    'b1': ' ',
    'c1': ' ',
    'a2': ' ',
    'b2': ' ',
    'c2': ' ',
    'a3': ' ',
    'b3': ' ',
    'c3': ' '
}

status = {
    'turn': True,
    'x_moves': [],
    'o_moves': [],
    'moves': ['a1','b1','c1','a2','b2','c2','a3','b3','c3'],
    'winning_combos': [
    ['a1', 'b1', 'c1'],
    ['a2', 'b2', 'c2'],
    ['a3', 'b3', 'c3'],
    ['a1', 'a2', 'a3'],
    ['b1', 'b2', 'b3'],
    ['c1', 'c2', 'c3'],
    ['a1', 'b2', 'c3'],
    ['c1', 'b2', 'c1']
    ]
}

display_board = '     a   b   c\n1)   {} | {} | {}   \n   -------------\n2)   {} | {} | {}   \n   -------------\n3)   {} | {} | {}   '.format(
    board['a1'],
    board['b1'],
    board['c1'],
    board['a2'],
    board['b2'],
    board['c2'],
    board['a3'],
    board['b3'],
    board['c3']
)


print(display_board)




def check_win(turn):
    if turn == 'x':
        for sublist in status['winning_combos']:
            if all(element in status['x_moves'] for element in sublist):
                print('X Player Wins')
                break
            else:
                move()
    else:
        for sublist in status['winning_combos']:
            if all(element in status['o_moves'] for element in sublist):
                print('O Player Wins')
                break
            else:
                move()

def move():
    if status['turn']:
        player_move = input('Player X move: ')
        if player_move in status['moves']:
            status['x_moves'].append(player_move)
            status['moves'].pop(status['moves'].index(player_move))
            board[player_move] = 'X'
            status['turn'] = False
            display_board = '     a   b   c\n1)   {} | {} | {}   \n   -------------\n2)   {} | {} | {}   \n   -------------\n3)   {} | {} | {}   '.format(
                board['a1'],
                board['b1'],
                board['c1'],
                board['a2'],
                board['b2'],
                board['c2'],
                board['a3'],
                board['b3'],
                board['c3']
            )
            print(display_board)
            check_win('x')
        else:
            print('error, move not avaiable, try again')
            move()
    else:
        player_move = input('Player O move: ')
        if player_move in status['moves']:
            status['o_moves'].append(player_move)
            status['moves'].pop(status['moves'].index(player_move))
            board[player_move] = 'O'
            status['turn'] = True
            display_board = '     a   b   c\n1)   {} | {} | {}   \n   -------------\n2)   {} | {} | {}   \n   -------------\n3)   {} | {} | {}   '.format(
                board['a1'],
                board['b1'],
                board['c1'],
                board['a2'],
                board['b2'],
                board['c2'],
                board['a3'],
                board['b3'],
                board['c3']
            )
            print(display_board)
            check_win('o')
        else:
            print('error, move not avaiable, try again')
            move()


move()
