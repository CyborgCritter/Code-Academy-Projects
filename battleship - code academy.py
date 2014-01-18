from random import randint 

board = []

def get_board_size():
    print ('\nThe board will be square.')
    print ('How many rows would you like the play field to be?')
    return get_number()
    
def get_num_turns():
    print ('\nHow many turns would you like the game to be?')
    return get_number()

def get_number():
    num=''
    while not num.isnumeric():
        num = input('please enter an integer')
        if num.isnumeric():
            return abs(int(num))

def make_board(lenAndWid, board):
    for i in range(lenAndWid):
        board.append(['O']*lenAndWid)
    
def print_board(board):
    print('\n')
    for row in range(len(board)):
        print (' '.join(board[row]))
    print('\n')
  
def random_coord(board):
    return randint(0, len(board)-1)

def get_int(board):
    userInput = input()
    if userInput.isnumeric():
        userInput = int(userInput)
        if userInput > 0 and userInput <= len(board):
            return (userInput-1)
    print ("Please enter a positive integer between 1 and " + str(len(board)) + ".\n")
    return (get_int(board)-1)

def check_guess(ship_row, ship_col, guess_row, guess_col, board, turn):
    if ship_row == guess_row and ship_col == guess_col:
        print ("Congratulations! You sank my battleship!")
        return (1)
    else:
        if guess_row > len(board)-1 or guess_col > len(board)-1:
            print ("Oops, that's not even in the ocean.")
        elif board[guess_row][guess_col] == 'X':
            print ("You guessed that one already.")
        else:
            print ("You missed my battleship!\n")
            board[guess_row][guess_col] = 'X'
            print_board(board)
        if turn >= 3:
            print ("\n\n\nGame Over\n\n\n")
        return (0)
    

lenAndWid = get_board_size()
numTurns = get_num_turns()
make_board(lenAndWid, board)


ship_row = random_coord(board)
ship_col = random_coord(board)


print_board(board)

for turn in range(numTurns):
    print ('\nTurn: ' + str(turn+1))
    print ('\nPlease enter an x coordinate to attack between 1 and ' + str(len(board)) + ".")
    guess_row = get_int(board)
    
    print ('\nPlease enter an y coordinate to attack between 1 and ' + str(len(board)) + ".")
    guess_col = get_int(board)
    
    winCheck = check_guess(ship_row, ship_col, guess_row, guess_col, board, turn)
    if winCheck == 1:
        break
