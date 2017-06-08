#!/bin/env python3
#
# https://www.hackerrank.com/challenges/python-string-split-and-join
#
# In Python, a string can be split on a delimiter.
#
# Example:
# #
# >>> a = "this is a string"
# >>> a = a.split(" ") # a is converted to a list of strings.
# >>> print a
# ['this', 'is', 'a', 'string']
# Joining a string is simple:
#
# >>> a = "-".join(a)
# >>> print a
# this-is-a-string
# Task
# You are given a string.
# Split the string on a " " (space) delimiter and join using a - hyphen.
#
# Input Format
# The first line contains a string consisting of space separated words.
#
# Output Format
# Print the formatted string as explained above.
#
# Sample Input
#
# this is a string
# Sample Output
#
# this-is-a-string


def split_and_join(s):
    """
    Strip off any trailing characters from the input s,
    split that on empty space into a list
    and join that list with '-' deliminter.
    Return the result.
    """
    return '-'.join(s.strip().split(' '))


if __name__ == '__main__':
    s = input()
    result = split_and_join(s)
    print(result)
