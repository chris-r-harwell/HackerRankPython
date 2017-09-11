#!/bin/env python3
#

# Given string S print all possible permutations
# of size k of the string in lexicogaphic sorted order.
#
# INPUT:
# S k
# where S is a string
# and k is an integer
# space separated
#
# OUTPUT:
# permutations of the string S
#


from itertools import permutations


if __name__ == '__main__':
    word, number = input().split(" ")
    number = int(number)

    perms1 = list(permutations(word, number))
    perms1.sort()

    [print(''.join(i)) for i in perms1]
