#!/bin/env python3
#
# combinations: for groups and order doesn't matter.
# permutations: for lists and order does matter.

# Given string S print all possible combinations
# of size k of the string in lexicogaphic sorted order.
#
# INPUT:
# S k
# where S is a string
# and k is an integer
# space separated
#
# OUTPUT:
# combinations of the string S
#


from itertools import combinations


if __name__ == '__main__':
    word, number = input().split(" ")
    word = sorted(word)
    number = int(number)

    for n in range(1, number + 1):
        for c in combinations(word, n):
            print(''.join(c))
