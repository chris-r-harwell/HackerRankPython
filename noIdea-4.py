#!/bin/env python3
"""
https://www.hackerrank.com/challenges/no-idea

There is an array of n integers. There are also 2 disjoint sets,
A and B each containing m integeres. You like all the integers in
set A and dislike all the integers in set B. Your initial happiness
is 0. For each i integer in the array, if i is an element of A, you
add 1 to your happiness. If i is an element of B, you add -1 to your
happiness. Otherwise, your happiness does not change. Output your final
happiness at the end.

Note: Since A and B are sets, they have no repeated elements. However,
the array might containt duplicate elements.

Constraints:

    1 <= n <= 10^5 1 <= m <= 10^5 1 <= any integer in the input <= 1-^9

INPUT:
    line: 1: integers n and m seperated by a space 2: n integers,
    elements of the array 3: m integers, A 4: m integers, B

OUTPUT:
    a single integer, your total happiness

"""

if __name__ == '__main__':
    input()  # skip the first line
    """ Create a dictionary and then put each set of integers
    into a label, events, positive or negative.
    Then add the number of elements in intersection of events and positive
    and subtract the number of elements in intersection of events and negative.
    Print. """
    a = dict()
    for label in 'events', 'positive', 'negative':
        a[label] = set(map(int, input().split()))
    # print(repr(a))
    print(len(a['positive'].intersection(a['events'])) -
          len(a['negative'].intersection(a['events'])))
