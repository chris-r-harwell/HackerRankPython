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

    ?

    1
    11 * 2
    111 * 3
    1111 * 4
    11111 * 5

Rules:
Use only arithmetic operations, a single for loop and a print statement.
Use no more than two lines.
Use nothing related to strings.


"""
j = 0
for i in range(1, int(input())):
    j = j + 10**(i - 1)
    print(i * j)
