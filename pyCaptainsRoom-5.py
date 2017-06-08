#!/bin/env python3
"""
https://www.hackerrank.com/challenges/py-the-captains-room

INPUT:
    lines:
    1: int K size of each group
    2: unordered elements of the room number list
Constraints:
    1 < K < 1000
OUPUT:
    The Captain's room number
"""
import collections


if __name__ == '__main__':
    k = int(input())
    rooms = collections.Counter(map(int, input().split()))
    # c.most_common()[:-n-1:-1]       # n least common elements
    cap = rooms.most_common()[:-2:-1]
    # above gets a [(X,1)]
    print(cap[0][0])
