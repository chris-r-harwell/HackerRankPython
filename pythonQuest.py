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


1 = 1
2 + 20  = 22
3 + 30 + 300 = 333
4 + 40 + 400 + 4000 =  4444
5 + 50 + 500 + 5000 + 50,000 = 55,555
...

1 * (10^0) = 1
2 + 2 * (10^1) = 22
3 + 3 * (10^1 + 10^2) = 333
4 + 4 * (10^1 + 10^2 + 10^3) = 4444
5 + 5 * (10^1 + 10^2 + 10^3 + 10^4) = 55555
...

1 * (10^0) = 1
2 * (10^0 + 10^1) = 22
3 * (10^0 + 10^1 + 10^2) = 333
4 * (10^0 + 10^1 + 10^2 + 10^3) = 4444
5 * (10^0 + 10^1 + 10^2 + 10^3 + 10^4) = 55555
...

Rules:
Use only arithmetic operations, a single for loop and a print statement.
Use no more than two lines.
Use nothing related to strings.


"""
j = 0
for i in range(1, int(input())):
    j += 10**(i - 1)
    print("{} {} {}".format(i, j, i * j))
