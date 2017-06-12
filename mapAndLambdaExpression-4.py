#!/bin/python3

"""
From https://en.wikipedia.org/wiki/Fibonacci_number
The sequence Fn of Fibonacci numbers is defined by the recurrence relation:

F_{n} = F_{n-1} + F_{n-2}

with seed values

F_{1} = 1, F_{2} = 1

or

F_{0} = 0, F_{1} = 1

Purpose: generate a list of the first N fibonacci numbers,
0 being the first number. Then, apply the map function and
a lambda expression to cube each fibonacci number and print
the list.

INPUT: integer N
Contraints 0 <= N <= 15
e.g. 5

OUTPUT: A list containing cubes of the first N fibonacci numbers.
e.g. [ 0, 1, 1, 8 ,27]
"""

def cube(x):
    return x ** 3


def fibonacci(n):
    """
    INPUT: int number of fibbonacci numbers to return
    OUTPUT: return a list of fibonacci numbers
    """
    fib_list = []
    if n == 0:
        fib_list = []
    elif n == 1:
        fib_list = [0]
    elif n >1:
        fib_list = [0, 1]
        for i in range(n - 2):
            fib_list.append(fib_list[-2] + fib_list[-1])

    print(repr(fib_list))
    return fib_list


if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))
