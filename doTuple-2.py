#!/bin/env python3

if __name__ == '__main__':
    # Read the number of ints in the list,
    #  but not used?
    # Map input string into a list of ints.
    # Create a tuple from the iterable list.
    # Calculate the hash and print.
    N = int(input())
    print(hash(tuple([int(i) for i in input().split()])))

