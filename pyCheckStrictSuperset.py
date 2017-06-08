#!/bin/env python3
"""
https://www.hackerrank.com/challenges/py-check-strict-superset

INPUT:
  lines:
  1: space sep. ele. of set A
  2: int. N, num. of other sets
  next N lines space sep. ele. of other sets.

Constraints:
    0 < len(set(A)) < 501
    0 < N < 21
    0 < len(otherSets) < 101

Task:
    determine if A is a strict superset of all other sets.
    e.g. that A must include elements of all other sets and at least one more.

OUTPUT:
    True or Falase
"""


def checkStrictSuperset(a, n):
    """
    They must mean check if a is a strict superset for each and every subsequent
    set b.
    So we read in set b and each time check criteria
    1) is it a superset? if not return false, otherwise continue.
    2) does a have elements b does not? if not return false, otherwise continue.
    """
    for i in range(n):
        b = set(map(int, input().split()))
        if not a.issuperset(b):
            return False
        if not any(a.difference(b)):
            return False

    return True


if __name__ == '__main__':
    """
    Read set a and the number of other sets,
    then pass that info to our check function
    and print the finding.
    """
    set_a = set(map(int, input().split()))
    n_other = int(input())
    print(checkStrictSuperset(set_a, n_other))
