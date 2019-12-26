theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ', 'mid-L': ' ', 'mid-M': '', 'mid-R': ' ', 'low-L': ' ',
            'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|')
    print('-+-+-')
    print(board['mid-L'] + '|')
    print('-+-+-')
    print(board['low-L'] + '|')


turn = 'X'

for i in range(9):
    printBoard(theBoard)
    print('Turn for ' + turn + '. Move on which space?')
    move = input()
    theBoard[move] = turn
    if turn == 'X':
        turn = 'O'
    else:
        turn = 'X'

printBoard(theBoard)
