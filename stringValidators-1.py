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


debug = True


def dprint(s):
    if debug:
        print(repr(s))


def print_characteristics(mydict, mylist ):
    """
    Print the dictionary in the order of mylist,
    using False if not present.
    """
    for c in mylist:
        print(mydict.get(c, False))


def validate_string( mydict, mylist, fullstring ):
    """
    Set attributes of fullstring contained in mylist in dictionary true
    if found for string or substring.
    """
    for characteristic in mylist:
        m = 'is' + characteristic
        for c in fullstring:
            res = getattr(c, m)()
            dprint(' checking {} got {} from {}'.format(m, res, c))
            if res:
                mydict[characteristic] = True
                dprint(' set {} to {}'.format( characteristic, mydict[characteristic]))
                break

    return


if __name__ == '__main__':
    string = input().strip()
    # Define the desired attributes of the string to charactetrize in an
    # ordered list, assume not in dictionary means false.
    characteristics_list = [ 'alnum', 'alpha', 'digit', 'lower', 'upper' ]
    string_characteristics = { }
    validate_string( string_characteristics, characteristics_list, string )
    print_characteristics( string_characteristics, characteristics_list )
