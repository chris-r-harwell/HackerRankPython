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
    # Read the number of elements from the first line and cast int,
    # unused.
    n = int(input())
    # Read the input, splitting up the numbers and mapping them as
    # integers into an iterable, then find the unique set of numbers
    # with set and sort that.
    # This should result in a unique set of sorted numbers.
    # The maximum would be at the end position, arr[-1]
    # The 2nd largest would be right before that, arr[-2]
    arr = sorted(set(map(int, input().split())))
    if len(arr) >= 2:
        print(arr[-2])
    else:
        print("Error: not enough unique numbers")
