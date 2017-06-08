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
debug = False


def dprint(s):
    if debug:
        print(repr(s))


def checkStrictSuperset(a, n):
    # set for accumulating the others
    b = set()

    for i in range(n):
        dprint(i)
        c = set(map(int, input().split()))
        dprint(c)
        # If the new set, c, is a subset of a,
        # then aggregate our new elements into b,
        # otherwise we know we do not have a superset
        # and return false.
        if a.issuperset(c):
            dprint("a is a superset of c")
            dprint("before {}".format(b))
            # b.update(c)
            b |= c
            dprint("after {}".format(b))
        else:
            dprint("a is not a superset of c")
            return False

    # make sure a is a superset of b
    # which it must be because we check on each iteration above....
    if a.issuperset(b):
        dprint("a is a superset of b")
        # then check and see if it is strict, containing
        # at least one element that b does not have.
        dprint(a.symmetric_difference(b))
        dprint(any(a.symmetric_difference(b)))
        if any(a.symmetric_difference(b)):
            return True
        else:
            return False
    else:
        dprint("a is not superset of b")
        return False


if __name__ == '__main__':
    """
    Read set a and the number of other sets,
    then pass that info to our check function
    and print the finding.
    """
    set_a = set(map(int, input().split()))
    dprint(set_a)
    n_other = int(input())
    dprint(n_other)
    print(checkStrictSuperset(set_a, n_other))
