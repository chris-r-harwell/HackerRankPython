#!/bin/env python3
#
# https://www.hackerrank.com/challenges/python-mutations
#
# We have seen that lists are mutable (they can be changed),
# and tuples are immutable (they cannot be changed).
#
# Task
# Read a given string,
# change the character at a given index and
# then print the modified string.
#
# Input Format
# The first line contains a string, S.
# The next line contains an integer i, denoting the index location
# and a character c separated by a space.
#
# Output Format
# Using any of the methods explained above,
# replace the character at index i with character c.
#
# Sample Input
# abracadabra
# 5 k

# Sample Output
# abrackdabra


def mutate_string(string, position, character):
    """
    Convert the string to a list, where each character is an element.
    change the value at the specified position to character.
    Return the result.
    """
    # s = list(string)
    # s[position] = character
    # new = ''.join(s)

    # OR Chop the input string from start to specified position,
    # add on the specified character,
    # add the last part of the chopped string, adding one to avoid
    # the character we are replacing.
    new = string[:position] + character + string[position + 1:]
    return new

if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)
