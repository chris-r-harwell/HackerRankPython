#!/bin/env python3
"""
https://www.hackerrank.com/challenges/triangle-quest-2

INPUT:
 integer N
 where 0 < N < 10

OUTPUT:
 print palindromic triangle of size N

 e.g.for N=5
1
121
12321
1234321
123454321

"""
for i in range(1, int(input()) + 1):
    left = [str(j) for j in range(1, i + 1)]
    right = [str(k) for k in range(i - 1, 0, -1)]
    print(''.join(left + right))
