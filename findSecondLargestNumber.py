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
    arr = map(int, input().split())
    ans_list = [i for i in arr]
    ans_list.sort()
    ans_list.reverse()
    largest = ans_list[0]
    for i in ans_list:
        if i < largest:
            print(i)
            break
