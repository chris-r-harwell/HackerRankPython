#!/bin/env python3
#


def minion_game(string):
    vowels = ('A', 'E', 'I', 'O', 'U')
    kevin = 0
    stuart = 0
    length = len(string)
    for start in range(0, length):
        for end in range(start + 1, length + 1):
            if s[start] in vowels:
                kevin += 1
            else:
                stuart += 1

    if stuart > kevin:
        print('Stuart {}'.format(stuart))
    elif kevin > stuart:
        print('Kevin {}'.format(kevin))
    else:
        print('Draw')


if __name__ == '__main__':
    s = input()
    minion_game(s)
