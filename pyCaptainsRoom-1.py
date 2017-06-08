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
def findCaptainsRoom(r):
    uniq = set(r)
    for i in uniq:
        if rooms.count(i) == 1:
            return i


if __name__ == '__main__':
    k = int(input())
    rooms = list(map(int,input().split()))
    cap = findCaptainsRoom(rooms)
    print(cap)
