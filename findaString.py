#!/bin/env python3
#
# https://www.hackerrank.com/challenges/find-a-string
#
# In this challenge, the user enters a string and a substring.
# You have to print the number of times that the substring occurs in the
# given string. String traversal will take place from left to right, not
# from right to left.
# NOTE: String letters are case-sensitive.
#
# Input Format
#  The first line of input contains the original string.
#  The next line contains the substring.
# Constraints
# 1<= len(string) <= 200
#  Each character in the string is an ascii character.
# Output Format
#  Output the integer number indicating the total number of occurrences
#  of the substring in the original string.
# Sample Input
#  ABCDCDC
#  CDC
# Sample Output
#  2
import re


debug = True


def dprint(s):
    if debug:
        print(repr(s))


def count_substring(string, substring):
    """
    Count number of times substring in string,
    using slices of substring length
    over the range of the string length.
    Return total count.
    Note: overlaps OK (string.count(s) is non-overlapping)
    """
    total = 0
    matches = re.findall('(?='+substring+')', string)
    dprint(matches)
    return len(matches)


if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_substring(string, sub_string)
    print(count)
