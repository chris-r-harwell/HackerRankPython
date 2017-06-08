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
    numb = input()
    lis = list(map(int, numb.split()))
    big, sbig = -6000, -6000
    for i in lis:
        if (i > big):
            big, sbig = i, big
        elif (i < big and i > sbig):
            sbig = i
    print (sbig)
