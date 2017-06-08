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
if __name__ == '__main__':
    # Read the first two lines, throwing away the integer
    # on the first and splitting the string by spaces on the second
    # then converting those into integers and placing them in a set M.
    # Do the same on the second two lines into set N.
    _, M = int(input()), set(map(int, input().split()))
    _, N = int(input()), set(map(int, input().split()))

    # Use the symmetric_difference function for sets to find it.
    result = N.symmetric_difference(M)

    # Then print an unpacked (*) list which has
    # been sorted using integers.
    # Use sep='\n' to put one per line.
    print(*sorted(result, key=int), sep='\n')
