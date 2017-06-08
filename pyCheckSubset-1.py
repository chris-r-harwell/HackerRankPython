#!/bin/env python3
"""
https://www.hackerrank.com/challenges/py-check-subset

You are given two sets, A and B
Your job is to find whether set A is a subset of set B

If set A is a subset of set B, print True
If set A is not a subset of set B, print False

INPUT:
    lines:
    1: number of test cases, T
    2: test cases, four lines ea
       a: num ele. of set A
       b: space sep. ele of A
       c: num ele. of set B
       d: space sep. ele. of B

Constraints:
    0 < T < 21
    0 < num. ele. in ea. set < 1001

OUTPUT:
    True or False for ea. test case on sep. lines.

"""


if __name__ == '__main__':
    n = int(input())
    for i in range(n):
        n_A = int(input())
        arr_A = set(map(int, input().split()))
        n_B = int(input())
        arr_B = set(map(int, input().split()))
        print(arr_A.issubset(arr_B))
