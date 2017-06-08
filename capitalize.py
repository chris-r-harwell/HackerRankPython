#!/bin/env python3
#
# REF: https://www.hackerrank.com/challenges/capitalize
#
# INPUT:
# a single line containing the string S.
# Contraint:
# 0 < len(S) < 1000
# string contains alphanumeric characters and spaces.
# OUTPUT:
# string capitalized, only the first character of each word.
#
#


def capitalize(s):
    """ Split the input string s into words in a list,
    capitalize them in a list comprehension,
    then join them back together with a space and
    return it.
    """
    # S = ' '.join([w.capitalize() for w in s.split()])
    # The above fails a couple of cases, maybe leading and trailing
    # and multiple spaces?

    """ Capitalize first character of each word, but keep
    track of word boundaries and keep spaces. """
    boundary = True

    S = ''
    for char in s:
        if char.isspace():
            boundary = True
            S += char
        elif boundary:
            boundary = False
            S += char.upper()
        else:
            boundary = False
            S += char
    return S


if __name__ == '__main__':
    string = input()
    capitalized_string = capitalize(string)
    print(capitalized_string)
