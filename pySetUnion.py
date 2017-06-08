#!/bin/env python3
"""

https://www.hackerrank.com/challenges/py-set-union

 .union() operator returns the union of a set and the set of elements in
 an iterable. Sometimes, the "|" operator is used in place of .union()
 operator, but it operates only on the set of elements in set. Set is
 immuatable to the .union() operation or ( | operation).

  |      (i.e. all elements that are in either set.)

Task:
    find ttl students subscribed to at least one newspaper, given tow
    lists of subscriptions
Input:
    lines 1: integer n, number of students subscribed to English
    newspaper 2: n space separated roll numbers of those students 3:
    integer b, number of students subscribed to Franch newspaper 4:
    b space separeated roll numbers of those students
Constraints:
    0 < ttl num students in college < 1000
Output:
    number who have at least one subscription

"""


if __name__ == '__main__':
    n = int(input())
    arrn = input().strip().split()
    b = int(input())
    arrb = input().strip().split()
    print(len(set(arrn).union(arrb)))
