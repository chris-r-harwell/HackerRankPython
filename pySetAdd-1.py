#!/bin/env python3
"""
https://www.hackerrank.com/challenges/py-set-add

Task Apply your knowledge of the .add() operation to help your friend
Rupal.

Rupal has a huge collection of country stamps. She decided to count the
total number of distinct country stamps in her collection. She asked
you for your help. You pick the stamps one by one from a stack of N
country stamps.

Find the total number of distinct country stamps.

INPUT:
line 1st: integer, N, total number of country stamps.  N lines:
contains the name of the country where the stamp is from.

Constraints:
0 < N < 1000

OUTPUT:
The total number of distinct country stamps on a single line.
"""


if __name__ == '__main__':
    stamps = set()
    n = int(input().strip())
    for i in range(n):
        stamps.add(input().strip())
    print(len(stamps))
