#!/bin/env python3

"""
https://www.hackerrank.com/challenges/python-mod-divmod

divmod(a, b)
 returns tuple ( a//b, a%b )
 where a//b is the integer division and
 a%b is the modulo operator getting remainder

INPUT: two lines
    int a
    int b

OUPUT: three lines
    result of integer division a//b
    result of modulo operator a%b
    prints the divmod of a and b ( a//b, a%b)
"""

a = int(input())
b = int(input())
res = divmod(a, b)
print("{}\n{}\n{}".format(res[0], res[1], res))
