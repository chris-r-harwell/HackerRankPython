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
    print(any([char.isalnum() for char in string]))
    print(any([char.isalpha() for char in string]))
    print(any([char.isdigit() for char in string]))
    print(any([char.islower() for char in string]))
    print(any([char.isupper() for char in string]))
