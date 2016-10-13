#! python3
#This program simulates a tick_Tack_Toe game by using a dictionay

import time

def printBoard(tempBoard):
    print(tempBoard['top-L'] + '|' + tempBoard['top-M'] + '|' + tempBoard['top-R'])
    print('-+-+-')
    print(tempBoard['mid-L'] + '|' + tempBoard['mid-M'] + '|' + tempBoard['mid-R'])
    print('-+-+-')
    print(tempBoard['low-L'] + '|' + tempBoard['low-M'] + '|' + tempBoard['low-R'])


board = {'top-L':' ', 'top-M': ' ', 'top-R':' ', 
         'mid-L':' ', 'mid-M': ' ', 'mid-R':' ',
         'low-L':' ', 'low-M': ' ', 'low-R':' '}

xPlayer = 0
while True:
    print ('Player #'+ str(xPlayer+1) +' make a move')
    position = input()
    if position == '':
        break
    if position in board:
        if xPlayer:
            board[position] = 'O'
        else:
            board[position] = 'X'
        xPlayer = ~xPlayer 
        printBoard(board)
    else:
        print ('wrong move try again')

#time.sleep(7)
