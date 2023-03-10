import random

game = True  # For the event loop

iteration = 0

board = [[1, 2, 3], [4, 'X', 6], [7, 8, 9]]  # Board

computer_choices_left = [
    board[0][0],
    board[0][1],
    board[0][2],
    board[1][0],
    board[1][2],
    board[2][0],
    board[2][1],
    board[2][2],
]  # These are the tile options for the computer to choose


# when a player selects a tile from
# 'board', the same tile gets deleted from this list


def display_board(board):
    print('                                 ')
    print('                                 ')
    print(f'             round {iteration}        ')
    print('                                 ')
    print('+----------+----------+----------+')
    print('|          |          |          |')
    print('|          |          |          |')
    print(f'|    {board[0][0]}     |    {board[0][1]}     |     {board[0][2]}    | ')
    print('|          |          |          |')
    print('+----------+----------+----------+')
    print('|          |          |          |')
    print('|          |          |          |')
    print(f'|    {board[1][0]}     |     {board[1][1]}    |     {board[1][2]}    |')
    print('|          |          |          |')
    print('|          |          |          |')
    print('+----------+----------+----------+')
    print('|          |          |          |')
    print('|          |          |          |')
    print(f'|    {board[2][0]}     |     {board[2][1]}    |     {board[2][2]}    |')
    print('|          |          |          |')
    print('|          |          |          |')
    print('+----------+----------+----------+')


def enter_move(board):
    player_input = int(input('Choose an empty tile: '))

    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == player_input:
                print(f'You chose: {board[i][j]}')
                computer_choices_left.remove(board[i][j])
                # removes tile chosen by player from computer_choice_left
                board[i][j] = 'O'  # lastly updates the board
                return


def draw_move(board):
    computer_input = random.choice(computer_choices_left)  # Picks random num from <-- var

    for i in range(len(board)):
        for j in range(len(board)):
            if board[i][j] == computer_input:
                print(f'Computer chose: {board[i][j]}')
                computer_choices_left.remove(board[i][j])
                # removes its self from the computer_choice_left list
                board[i][j] = 'X'  # updates in the board
                return


# All the functions are called in the event loop so
# first the board is displayed with 5 always marked out as it's the first choice
# the computer makes by default, so its set permanently to X

# Second the enter_move function is called to handle player input and modify the board

# third the computer runs its random selection from the available blank spaces
# left in 'computer_choice_left' and updates the board


while game:
    iteration += 1 #just displays the current round

    display_board(board)
    enter_move(board)
    draw_move(board)


    t1 = board[0][0] == 'O'
    t1x = board[0][0] == 'X'
    t2 = board[0][1] == 'O'
    t2x = board[0][1] == 'X'
    t3 = board[0][2] == 'O'
    t3x = board[0][2] == 'X'
    t4 = board[1][0] == 'O'
    t4x = board[1][0] == 'X'
    t5 = board[1][1] == 'O'
    t5x = board[1][1] == 'X'
    t6 = board[1][2] == 'O'
    t6x = board[1][2] == 'X'
    t7 = board[2][0] == 'O'
    t7x = board[2][0] == 'X'
    t8 = board[2][1] == 'O'
    t8x = board[2][1] == 'X'
    t9 = board[2][2] == 'O'
    t9x = board[2][2] == 'X'

#decides the outcome of the game

    if t1 and t2 and t3:
        display_board(board)
        game = False
        print('You won!     case 1')

    elif t1x and t2x and t3x:
        display_board(board)
        game = False
        print('The computer won    case 1')

    elif t1 and t4 and t7:
        display_board(board)
        game = False
        print('You won! case 2')
    elif t1x and t4x and t7x:
        display_board(board)
        game = False
        print('The computer won    case 2')

    elif t7 and t8 and t9:
        display_board(board)
        game = False
        print('You won! case 3')
    elif t7x and t8x and t9x:
        display_board(board)
        game = False
        print('The computer won    case 3')

    elif t3 and t6 and t9:
        display_board(board)
        game = False
        print('You won!    case 4')
    elif t3x and t6x and t9x:
        display_board(board)
        game = False
        print('The computer won    case 4')

    elif (t1x and t5x and t9x) or (t3x and t5x and t7x) or (t4x and t5x and t6x):
        display_board(board)
        game = False
        print('The computer won    case 5')

    elif len(computer_choices_left) < 2:
        display_board(board)
        game = False
        print('Game Locked. Start New Game')
