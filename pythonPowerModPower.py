#!/bin/env python3
"""
https://www.hackerrank.com/challenges/python-power-mod-power

power or exponents
pow(a, b)
same as a**b

also possible to calculare a^b mod m.
for printing resultant %mod.

Mote: here a and b can be floats or negative,
  but if a third arguement is present b cannot be negative.

Note: there is a math.pow() too, rarely used.

INPUT: three lines
 int a
 int b
 int m

 1 <= a,b <= 10
 2 <= m <= 1000

OUTPUT: two lines
 pow(a, b)
 pow(a, b, m)
"""
a = int(input())
b = int(input())
m = int(input())
# print(pow(a, b))
# print( a**b )
p = a**b
n = p % m
print(p)
# print(pow(a, b, m))
# print( a**b % m )
print(n)
