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
    ],
    'x_score': 0,
    'o_score': 0,
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

def reset_game():
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

def play_again(turn):
    ask_rematch = input('Play again? (y / n): ')
    if ask_rematch == 'y':
        reset_game()
        print(display_board)
        move(turn)
    else:
        print('Thank you for playing!')
        exit()

def display_score():
    print('X: {}   -   O: {}'.format(status['x_score'], status['o_score']))


def check_win(turn):
    for sublist in status['winning_combos']:
        if any(set(sublist).issubset(status['{}_moves'.format(turn)]) for sublist in status['winning_combos']):
            print('{} PLAYER WINS'.format(turn.capitalize()))
            status['{}_score'.format(turn)] += 1
            display_score()
            if turn == 'x':
                play_again('o')
            else:
                play_again('x')
        else:
            if turn == 'x':
                move('o')
            else:
                move('x')

def move(turn):
    if len(status['moves']) == 0:
        display_score()
        print('TIE GAME')
        play_again('x')
    player_move = input('Player {} move: '.format(turn.capitalize()))
    if player_move in status['moves']:
        status['{}_moves'.format(turn)].append(player_move)
        status['moves'].pop(status['moves'].index(player_move))
        status['board'][player_move] = turn.capitalize()
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
        check_win(turn)
    else:
        print('error, move not avaiable, try again')
        move(turn)

print(" ----------------------\n Let's play Py-Pac-Poe!\n ----------------------")
print(display_board)
move('x')
