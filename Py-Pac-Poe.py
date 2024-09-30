print(" ----------------------\n Let's play Py-Pac-Poe!\n ----------------------")



status = {
    'board':{
    'a1': ' ',
    'b1': ' ',
    'c1': ' ',
    'a2': ' ',
    'b2': ' ',
    'c2': ' ',
    'a3': ' ',
    'b3': ' ',
    'c3': ' '
    },
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
    ['c1', 'b2', 'a3']
    ]
}

display_board = '     a   b   c\n1)   {} | {} | {}   \n   -------------\n2)   {} | {} | {}   \n   -------------\n3)   {} | {} | {}   '.format(
    status['board']['a1'],
    status['board']['b1'],
    status['board']['c1'],
    status['board']['a2'],
    status['board']['b2'],
    status['board']['c2'],
    status['board']['a3'],
    status['board']['b3'],
    status['board']['c3']
)


print(display_board)


def play_again():
    ask_rematch = input('Play again? (y / n): ')
    if ask_rematch == 'y':
        status['turn'] = True
        status['x_moves'] = []
        status['o_moves'] = []
        status['moves'] = ['a1','b1','c1','a2','b2','c2','a3','b3','c3']
        status['board'] = {
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
        print(display_board)
        move()
    else:
        exit()


def check_win(turn):
    if turn == 'x':
        for sublist in status['winning_combos']:
            if any(set(sublist).issubset(status['x_moves']) for sublist in status['winning_combos']):
                print('X PLAYER WINS')
                play_again()
            else:
                move()
    else:
        for sublist in status['winning_combos']:
            if any(set(sublist).issubset(status['o_moves']) for sublist in status['winning_combos']):
                print('O PLAYER WINS')
                play_again()
            else:
                move()

def move():
    if len(status['moves']) == 0:
        print('TIE GAME')
        play_again()
    if status['turn']:
        player_move = input('Player X move: ')
        if player_move in status['moves']:
            status['x_moves'].append(player_move)
            status['moves'].pop(status['moves'].index(player_move))
            status['board'][player_move] = 'X'
            status['turn'] = False
            display_board = '     a   b   c\n1)   {} | {} | {}   \n   -------------\n2)   {} | {} | {}   \n   -------------\n3)   {} | {} | {}   '.format(
                status['board']['a1'],
                status['board']['b1'],
                status['board']['c1'],
                status['board']['a2'],
                status['board']['b2'],
                status['board']['c2'],
                status['board']['a3'],
                status['board']['b3'],
                status['board']['c3']
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
            status['board'][player_move] = 'O'
            status['turn'] = True
            display_board = '     a   b   c\n1)   {} | {} | {}   \n   -------------\n2)   {} | {} | {}   \n   -------------\n3)   {} | {} | {}   '.format(
                status['board']['a1'],
                status['board']['b1'],
                status['board']['c1'],
                status['board']['a2'],
                status['board']['b2'],
                status['board']['c2'],
                status['board']['a3'],
                status['board']['b3'],
                status['board']['c3']
            )
            print(display_board)
            check_win('o')
        else:
            print('error, move not avaiable, try again')
            move()


move()
