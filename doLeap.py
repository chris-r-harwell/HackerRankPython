#!/bin/env python3


def is_leap(year):
    # The year can be evenly divided by 4, unless;
    leap = False
    if (year % 4 != 0):
        return leap

    leap = True
    # The year can be evenly divided by 100, it is NOT a leap year, unless;
    if (year % 100 == 0):
        leap = False

    # The year is also evenly divisible by 400. Then it is a leap year.
    if (year % 400 == 0):
        leap = True

    return leap

if __name__ == '__main__':
    year = int(input())
    print(is_leap(year))
