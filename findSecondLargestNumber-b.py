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
    n = int(input())
    collection = set(map(int, input().split()))
    collection.remove(max(collection))
    print(max(collection))
