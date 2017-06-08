#!/bin/env python3
#
# hackerrank.com
# https://www.hackerrank.com/challenges/find-second-maximum-number-in-a-list
#
# INPUT: first line N
#        second line array A[] of N integers each seperated by a space.
# OUTPUT: The value of the second largest number.
#


if __name__ == '__main__':
    # Read the number of elements from the first line, not used.
    num = int(input())
    # Make a list from strings split and mapped as integers into
    # an interable.
    arr = list(map(int, input().split()))
    print(max([a for a in arr if a != max(arr)]))

