#!/bin/env python3
"""

defaultdict tool is a containter in the collections class of Python.
It is similar to the usual dictionary (dict) container, but it has one
difference: The value fields' data type is specified upon initialization.

INPUT: 1 + n + m lines
 int n and m
 next n lines:
   words belonging to group A
 next m lines:
   words belonging to group B

For each group B word,
 find position in the group A list
 pos1 pos2 pos3


OUTPUT: m lines
 ea. line should contain the positions of the occurences of
 group B word in the group A list separated by spaces.
 Print the indices of ea. occurrence of m in group A.
 If it does not appear, print -1.

"""


import collections


if __name__ == '__main__':
    """
    Read in n and m
    the number of expected words in group A and
    group B.
    Create a dictionary of lists for the positions.
    While reading in group A note the positions,
    (zero index + 1) into the dictionary.
    While reading in group B look for the word,
    and print the positions.
    """
    n, m = map(int, input().split())
    positions = collections.defaultdict(list)
    for i in range(n):
        word = input()
        positions[word].append(i + 1)
    for i in range(m):
        word = input()
        p = positions.get(word, -1)
        print(*p)
