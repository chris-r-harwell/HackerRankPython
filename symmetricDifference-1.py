#!/bin/env python3
"""
https://www.hackerrank.com/challenges/symmetric-difference

Task:
    Given 2 sets of integers, M and N, print their symmetric difference
    in ascending order. The term symmetric difference indicates those values
    that exist in either M or N but do not exist in both.

INPUT:
    lines:
    1st: integer M
    2nd: M space-seperated integers.
    3rd: integer N
    4th: N space-seperated integers.

OUTPUT:
    symmetric difference integers in ascending order, one per line.
"""


def average(array):
    u = set(array)
    return sum(u)/len(u)


if __name__ == '__main__':
    res = []
    num_M_elements = int(input())
    M = set(list(map(int, input().split())))
    num_N_elements = int(input())
    N = set(list(map(int, input().split())))
    res = [i for i in M.difference(N)]
    for i in N.difference(M):
        res.append(i)
    res.sort()
    for i in res:
        print(i)
