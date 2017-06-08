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
import re


debug = False


def dprint(s):
    if debug:
        print(repr(s))


def print_string_attrs(mydict, mylist):
    """
    Print the dictionary in the order of mylist, False if not present.
    """
    for c in mylist:
        print(mydict.get(c, False))


def get_string_attrs(d, attrs, s):
    """
    Set attributes to True in dictionary d if true for any character in
    string s.
    Attributes are contained in list attrs and match the method name
    for the string class, without the 'is' which we add.
    """
    if re.search('[A-Z]', s):
        d['upper'] = True # 5

    if re.search('[a-z]', s):
        d['lower'] = True # 4

    if re.search('[0-9]', s):
        d['digit'] = True # 3
        d['alnum'] = True # 1

    if d.get('upper', False) or d.get('lower', False):
        d['alnum'] = True # 1
        d['alpha'] = True # 2

    return


if __name__ == '__main__':
    string = input().strip()
    # Define the desired attributes of the string to characterize in an
    # ordered list, assuming not in dictionary means false.
    attrs_list = ['alnum', 'alpha', 'digit', 'lower', 'upper']
    attrs_dict = {}
    get_string_attrs(attrs_dict, attrs_list, string)
    print_string_attrs(attrs_dict, attrs_list)

if __name__ == '__main__':
    string = input().strip()
    patterns = ['[A-Za-z0-9]', '[A-Za-z]', '[0-9]', '[a-z]', '[A-Z]']
    # interestingly if
    # 5 True, then 1 and 2 True
    # 4 True, then 1 and 2 True
    # 3 True, then 1 True
