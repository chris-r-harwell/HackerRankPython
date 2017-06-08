#!/bin/env python3
"""
https://www.hackerrank.com/challenges/py-introduction-to-sets

A set is an unordered collection of elements _without_ duplicate entries.
When printed, iterated or converted into a sequence, its elements will
appear in an arbitrary order.

Basically, sets are used for membership testing and eliminating duplicate
entries.

Task:

    Now, let's use our knowledge of sets and help Mickey.

    Ms. Gabriel Williams is a botany professor at District College. One
    day, she asked her student Mickey to compute the average of all the
    plants with distinct heights in her greenhouse.

    Formula used:

    Average = Sum of Distinct Heights / Total Number of Distinct Heights

INPUT:
    1st line: integer, N, the total number of plants.  2nd line: N,
    space separated heights of the plants.

Contraints:
    0 < N <= 100

OUTPUT:
    average height value on a single line.
"""


def average(array):
    u = set(array)
    return sum(u)/len(u)


if __name__ == '__main__':
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
