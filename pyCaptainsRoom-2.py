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


if __name__ == '__main__':
    k = int(input())
    rooms = tuple(map(int, input().split()))
    for i in set(rooms):
        if rooms.count(i) == 1:
            print(i)
