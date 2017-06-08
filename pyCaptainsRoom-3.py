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
    rooms = list(map(int, input().split()))
    """
    Sort the list, split it into halves,
    and find the symmetric difference between 
    them, leaving the number which only occurs in
    one list.
    """
    rooms.sort()
    print(*(set(rooms[::2]) ^ set(rooms[1::2])))
