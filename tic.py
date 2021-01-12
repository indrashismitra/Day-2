import sys
pos1 = ' '
pos2 = ' '
pos3 = ' '
pos4 = ' '
pos5 = ' '
pos6 = ' '
pos7 = ' '
pos8 = ' '
pos9 = ' '

p1 = '1'
p2 = '2'
p3 = '3'
p4 = '4'
p5 = '5'
p6 = '6'
p7 = '7'
p8 = '8'
p9 = '9'

a = '  {}  |  {}  |  {}'.format(pos1, pos2, pos3)
b = '-----|-----|-----'
c = '  {}  |  {}  |  {}'.format(pos4, pos5, pos6)
d = '-----|-----|-----'
e = '  {}  |  {}  |  {}'.format(pos7, pos8, pos9)

first_player_letter = 'X'
current_letter = 'X'
first = True

def play(letter, position):
    global pos1, pos2, pos3, pos4, pos5, pos6, pos7, pos8, pos9, a, b, c, d, e, p1, p2, p3, p4, p5, p6, p7, p8, p9
    if letter == 'X' or letter == 'O':
        if position == '1':
            if pos1 == ' ':
                pos1 = letter
                p1 = pos1
        if position == '2':
            if pos2 == ' ':
                pos2 = letter
                p2 = pos2
        if position == '3':
            if pos3 == ' ':
                pos3 = letter
                p3 = pos3
        if position == '4':
            if pos4 == ' ':
                pos4 = letter
                p4 = pos4
        if position == '5':
            if pos5 == ' ':
                pos5 = letter
                p5 = pos5
        if position == '6':
            if pos6 == ' ':
                pos6 = letter
                p6 = pos6
        if position == '7':
            if pos7 == ' ':
                pos7 = letter
                p7 = pos7
        if position == '8':
            if pos8 == ' ':
                pos8 = letter
                p8 = pos8
        if position == '9':
            if pos9 == ' ':
                pos9 = letter
                p9 = pos9
        if (pos1 == pos5 == pos9 or pos1 == pos2 == pos3 or pos1 == pos4 == pos7) and pos1 != ' ':
            print(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n\n')
            if first_player_letter in pos1: # TODO
                print('Congratulations, Player 1! You have won!')
                start_game()
            else:
                print('Congratulations, Player 2! You have won!')
                start_game()
        if pos2 == pos5 == pos8 and pos2 != ' ':
            print(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n\n')
            if first_player_letter in pos2:
                print('Congratulations, Player 1! You have won!')
                start_game
            else:
                print('Congratulations, Player 2! You have won!')
                start_game()
        if (pos3 == pos5 == pos7 or pos3 == pos6 == pos9) and pos3 != ' ':
            print(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n\n')
            if first_player_letter in pos3:
                print('Congratulations, Player 1! You have won!')
                start_game()
            else:
                print('Congratulations, Player 2! You have won!')
                start_game()
        if pos4 == pos5 == pos6 and pos4 != ' ':
            print(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n\n')
            if first_player_letter in pos4:
                print('Congratulations, Player 1! You have won!')
                start_game()
            else:
                print('Congratulations, Player 2! You have won!')
                start_game()
        if pos7 == pos8 == pos9 and pos7 != ' ':
            print(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n\n')
            if first_player_letter in pos7:
                print('Congratulations, Player 1! You have won!')
                start_game()
            else:
                print('Congratulations, Player 2! You have won!')
                start_game()
        if pos1 != ' ' and pos2 != ' ' and pos3 != ' ' and pos4 != ' ' and pos5 != ' ' and pos6 != ' ' and pos7 != ' ' and pos8 != ' ' and pos9 != ' ':
            print(a + '\n' + b + '\n' + c + '\n' + d + '\n' + e + '\n\n')
            print('Sorry, no one won! We have a draw! Better luck next time.')
            start_game()
        tic_tac_toe()

    else:
        return

def start_game():
    global first_player_letter
    global current_letter
    letter = input('Player 1, what character do you wish to play with? (X or O) :')
    if letter == 'X' or letter == 'O':
        if letter == 'O':
            first_player_letter = 'O'
        current_letter = letter
        tic_tac_toe()
    else:
        print('Please type X or O')
        start_game()

def tic_tac_toe():
    global current_letter
    global first
    if not first:
        if current_letter == 'X':
            current_letter = 'O'
        else:
            current_letter = 'X'
    first = False
    print('  {}  |  {}  |  {}\n-----|-----|-----\n  {}  |  {}  |  {}\n-----|-----|-----\n  {}  |  {}  |  {}\n\n'.format(p1, p2, p3, p4, p5, p6, p7, p8, p9))
    position = input('Select a position to place your piece at: (1 - 9) ')
    try:
        if int(position) > 0 and int(position) < 10:
            play(current_letter, position)
        else:
            print('Please type a valid number from 1 - 9.')
            first = True
            tic_tac_toe()
    except:
        print('Please type a valid number from 1 - 9.')
        first = True
        tic_tac_toe()

if __name__ == '__main__':
    start_game()