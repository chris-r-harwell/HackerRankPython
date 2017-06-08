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
    """ Accumulate other sets into set b,
    then check the two criteria for a strict 
    superset:
    1) a is a superset of b,
    2) a contains elements not in b
    """
    b = set()

    for i in range(n):
        b |= set(map(int, input().strip().split()))

    if a.issuperset(b):
        if any(a.symmetric_difference(b)):
            return True

    return False


if __name__ == '__main__':
    """
    Read set a and the number of other sets,
    then pass that info to our check function
    and print the finding.
    """
    set_a = set(map(int, input().strip().split()))
    n_other = int(input().strip())
    print(checkStrictSuperset(set_a, n_other))
