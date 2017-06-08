#!/bin/env python3
"""
https://www.hackerrank.com/challenges/python-quest-1

INPUT:
    int N, where 1 <= N <= 9

OUTPUT: N-1 lines
    numerical triangle of height N-1 like
    1
    22
    333
    4444
    55555
    ...

Rules:
Use only arithmetic operations, a single for loop and a print statement.
Use no more than two lines.
Use nothing related to strings.


"""
for i in range(1, int(input())):
    j = 0
    while j < i:
        print(i, end='')
        j += 1
    print()
