#!/bin/env python3
"""
https://www.hackerrank.com/challenges/py-set-mutations

Task: given set A and N number of other sets. These N number of sets
have to perform some specific mutation operations on set A.

Your task is to execute those operations and print the sum of elements
from set A.

Input Format:
    lines:
    1 int num of ele in set A
    2 space separated list of ele in set A
    3 int N number of other sets
    4 .. 4+ 2*N lines
      a) space separated entries of the operation name and len of other set
      b) space separated list of ele in other set

0 < len(set(A)) < 10^3
0 < len(otherSets) < 10^3
0 < N < 10^3

Output:
    sum of ele in set A (after mutations)
"""
debug = False


def dprint(s):
    if debug:
        print(repr(s))


def mutateSet(A, operation, B):
    if operation == "update":
        # A.update(B)
        A |= B
    elif operation == "intersection_update":
        # A.intersection_update(B)
        A &= B
    elif operation == "difference_update":
        # A.difference_update(B)
        A -= B
    elif operation == "symmetric_difference_update":
        # A.symmetric_difference_update(B)
        A ^= B
    else:
        raise KeyError


if __name__ == '__main__':
    n_A = int(input())
    dprint(n_A)
    arr_A = set(map(int, input().split()))
    dprint(arr_A)
    n_other = int(input())
    for i in range(n_other):
        line = input().split()
        op, n_B = line[0], int(line[1])
        arr_B = set(map(int, input().split()))
        dprint(op)
        dprint(n_B)
        dprint(arr_B)
        mutateSet(arr_A, op, arr_B)
        dprint("new {}".format(arr_A))
    print(sum(arr_A))
