#!/bin/env python3
#
# https://www.hackerrank.com/challenges/string-validators
#
# Task
# Find out if the string S contains:
# alphanumeric characters,
# alphabetical characters,
# digits,
# lowercase and
# uppercase characters.
# NOTE: String letters are case-sensitive.
#
# Input Format
#  A single line containting a string S.
# Constraints
# 1<= len(string) <= 1000
# Output Format
# 5 lines:
#  1st: print True if S has any alphanum, otherwise False.
#  2nd: print True if S has any alphabetical, otherwise False.
#  3rd: print True if S has any digits, otherwise False.
#  4th: print True if S has any lowercase characters, otherwise print False.
#  5th: print True if S has any uppercase characters, otherwise print False.
# Sample Input
#  qA2
# Sample Output
# True
# True
# True
# True
# True


if __name__ == '__main__':
    string = input().strip()
    """
    Checking each attibute in the list,
    'alnum', 'alpha', 'digit', 'lower', 'upper'
    get the result of the string method using getattr with a list comprehension
    over each character in the string.
    Use the any function to return True if any True, otherwise False.
    """
    for a in ['alnum', 'alpha', 'digit', 'lower', 'upper']:
        m = 'is' + a
        print(any([getattr(c, m)() for c in string]))
