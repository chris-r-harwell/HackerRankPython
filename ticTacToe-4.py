#!/bin/env python3
#
# ticTacToe.py
#
# From _Automate the Boring Stuff with Python_,
#  Using Data Structures to Model Real-World Things,
#  p. 113
#
#   Tic Tac Toe

#   top-L | top-M | top-R
#   ---------------------
#   mid-L | mid-M | mid-R
#   ---------------------
#   low-L | low-M | low-R
#

import pprint


theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}

theBoardWithKeys = {'top-L': 'top-L', 'top-M': 'top-M', 'top-R': 'top-R',
                    'mid-L': 'mid-L', 'mid-M': 'mid-M', 'mid-R': 'mid-R',
                    'low-L': 'low-L', 'low-M': 'low-M', 'low-R': 'low-R'}

def printBoard(board):
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print()


def printBoardLegend(board):
    print()
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-----+-----+-----')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-----+-----+-----')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])
    print()


def makeMove(board, turn):
    valid = False
    keyList = list(board.keys())
    keyList.sort()

    while not valid:
        printBoard(board)
        print('Turn for ' + turn + '. Move on which space?' + str(keyList))
        move = input()
        # Check if the move label is a valid dictionary key.
        if move in board.keys():
            # Check if space open.
            if board.get(move, ' ') == ' ':
                valid = True
                return move
            else:
                err = 'Try again: your move ' + move
                err = err + ' already taken.'
                print(err)
        else:
            err = 'Try again: your move ' + move
            err = err + ' not found in ' + str(keyList)
            print(err)
            printBoard(theBoardWithKeys)


def checkWin(board):
    for turn in 'X' 'O':
        # across
        if board['top-L'] == board['top-M'] == board['top-R'] == turn:
            return turn
        if board['mid-L'] == board['mid-M'] == board['mid-R'] == turn:
            return turn
        if board['low-L'] == board['low-M'] == board['low-R'] == turn:
            return turn
        # down
        if board['top-L'] == board['mid-L'] == board['low-L'] == turn:
            return turn
        if board['top-M'] == board['mid-M'] == board['low-M'] == turn:
            return turn
        if board['top-R'] == board['mid-R'] == board['low-R'] == turn:
            return turn
        # diaganol
        if board['top-L'] == board['mid-M'] == board['low-R'] == turn:
            return turn
        if board['top-R'] == board['mid-M'] == board['low-L'] == turn:
            return turn


def playGame():
    turn = 'X'
    for i in range(9):
        move = makeMove(theBoard, turn)
        theBoard[move] = turn
        printBoard(theBoard)
        winner = checkWin(theBoard)
        if winner:
            print('Player ' + winner + ' wins!')
            break
        if turn in theBoard.get(move):
            if turn == 'X':
                turn = 'O'
            else:
                turn = 'X'


    if not winner:
        print('Game over: tie.')


play = 'y'
while 'y' in play:
    printBoardLegend(theBoardWithKeys)
    playGame()
    print('Would you like to play tic-tac-toe?')
    play = input().lower()
