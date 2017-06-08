#!/bin/env python3
#


def merge_the_tools(string, k):
    n = len(string)
    # parts = n // k
    # print('string: {}'.format(string))
    # print('string length: {}'.format(n))
    # print('{} blocks of {} characters'.format(parts, k))
    letters = {}
    for start in range(0, n - k + 1, k):
        end = start + k
        # print('start: {}'.format(start))
        # print('end: {}'.format(end))
        # print(string[start:end])
        mylist = []
        for c in string[start:end]:
            # print('checking char {}:'.format(c))
            if c not in mylist:
                mylist.append(c)
        print(''.join(mylist))


if __name__ == '__main__':
    """
From https://www.hackerrank.com/challenges/merge-the-tools

Consider the following:

    a string, s, of length n where s = c_0c_1...c_(n-1)
    an integer, k, where k is a factor of n.

We can split s into n/k subsegments where each subsegment, t_i, consists
of a contiguous block of k characters in s. Then, use t_i to create string
u_i such that:

    the characters in u_i are a subsequence of the characters in t_i
    any repeat occurrence of a character is removed from the string such
    that each character in u_i occurs exactly once. In other words, if the
    character at some index j in t_i occurs at a previous index < j in
    t_i, then do not include the character in string u_i.

    Given s and k print n/k lines where each line i denots string u_i.


INPUT:
    first line: a string s of length where s = c_0,c_1...c_)n-1)
    second line: integer k, length of each subsegment

Constraints:
    1 <= n <= 10^4, where n is the length of s
    1 <= k <= n
    guaranteed that n is a multiple of k

OUTPUT:
    print n/k lines where each line i contains string u_i


    read string and int
    split the string into n/k subsegments
    use each subsegment to make a string with
    no subsequent repeated characters.

    Example:
    AABCAAADA
    3

    len(s) = 9
    9/3 = 3
    AAB -> AB
    CAA -> CA
    ADA -> AD
    """
    string, k = input(), int(input())
    merge_the_tools(string, k)
