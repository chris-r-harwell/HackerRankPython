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
    # Find the maxium value in the list.
    m = max(arr)
    # Filter the list to get those less than the maximum.
    ans_list = [x for x in arr if x < m]
    # Get the maximum of the new list and pring.
    next_largest = max(ans_list)
    print(next_largest)
