#!/bin/env python3
"""

https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation

Input:
    lines 1: integer n, number of students subscribed to English
    newspaper 2: n space separated roll numbers of those students 3:
    integer b, number of students subscribed to French newspaper 4:
    b space separeated roll numbers of those students
Constraints:
    0 < ttl num students in college < 1000
Output:
    number who only subscribe to one, either English or French

"""
debug = False


def dprint(s):
    if debug:
        print(repr(s))


if __name__ == '__main__':
    n = int(input())
    arrn = input().strip().split()
    b = int(input())
    arrb = input().strip().split()
    dprint(n)
    dprint(arrn)
    dprint(b)
    dprint(arrb)
    print(len(set(arrn).symmetric_difference(arrb)))
