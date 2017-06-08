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
theBoard = {'top-L': ' ', 'top-M': ' ', 'top-R': ' ',
            'mid-L': ' ', 'mid-M': ' ', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': ' '}


def printBoard(board):
    print(board['top-L'] + '|' + board['top-M'] + '|' + board['top-R'])
    print('-+-+-')
    print(board['mid-L'] + '|' + board['mid-M'] + '|' + board['mid-R'])
    print('-+-+-')
    print(board['low-L'] + '|' + board['low-M'] + '|' + board['low-R'])


printBoard(theBoard)

theBoard = {'top-L': 'O', 'top-M': 'O', 'top-R': 'O',
            'mid-L': 'X', 'mid-M': 'X', 'mid-R': ' ',
            'low-L': ' ', 'low-M': ' ', 'low-R': 'X'}
printBoard(theBoard)
