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
    # If we had k rooms of each room number then this would be the sum:
    k_sum = sum(set(rooms)) * k
    # We do not, so this is the sum:
    j_sum = sum(rooms)
    # Then, k_sum - j_sum should be captains room number * (k-1).
    # So, divide by k-1 to get the capt rm number:
    cap = (k_sum - j_sum) / (k - 1)
    print("{:.0f}".format(cap))
