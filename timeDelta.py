#!/bin/env python3
#
# REF: https://docs.python.org/3/library/datetime.html#module-datetime
#


from datetime import datetime
# Day dd Mon yyyy hh:mm:ss +xxxx
# Sun 10 May 2015 13:54:36 -0700
DATETIME_FORMAT = '%a %d %b %Y %H:%M:%S %z'


if __name__ == '__main__':
    """
    For some number of cases read as the first line of input
    read two lines each specifing a time date format. Convert those
    to Python datatime objects according to a standard format and
    then find the number of seconds between them, printing the
    whole number absolute value.
    """
    number_of_cases = int(input())
    # print('number of cases: {}'.format(number_of_cases))
    for _ in range(number_of_cases):
        s1 = input()
        # print('string 1: {}'.format(s1))
        t1 = datetime.strptime(s1, DATETIME_FORMAT)
        # print('time 1: {}'.format(t1))
        s2 = input()
        # print('string 2: {}'.format(s2))
        t2 = datetime.strptime(s2, DATETIME_FORMAT)
        # print('time 1: {}'.format(t2))
        diff = t1 - t2
        print('{:.0f}'.format(abs(diff.total_seconds())))
