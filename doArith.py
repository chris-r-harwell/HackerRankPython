#!/bin/env python3


def doArith(a, b):
    # Task
    # Read two integers from STDIN and print three lines where:
    # The first line contains the sum of the two numbers.
    print(a + b)
    # The second line contains the difference of the two numbers
    # (first - second).
    print(a - b)
    # The third line contains the product of the two numbers.
    print(a * b)


if __name__ == '__main__':
    a = int(input())
    b = int(input())
    doArith(a, b)
