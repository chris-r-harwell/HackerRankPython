#!/bin/env python3
"""
Counter - a containter that stores elements as dictionary keys,
and their counts are stored as dictionary values.

INPUT:
    X, number of shoes
    shoe_size_array, list of all shoe sizes in shop
    N, number of customers
    next N lines two space separated values:
       s p
       shoe size price of shoe

OUTPUT:
    Amount of money earned
"""


import collections

if __name__ == '__main__':
    """
    Read the number of shoes, the size list and the number
    of customers.
    Then confirm size list has correct number of items.
    Then convert size list into a collection.
    For each customer read the size and price
      if size in stock add price to money earned
      and remove from inventory.
    """
    X = int(input())
    size_list = list(map(float, input().split()))
    N = int(input())

    assert X == len(size_list)
    inventory = collections.Counter(size_list)
    money = 0.0

    for i in range(N):
        s, p = map(float, input().split())
        if inventory.get(s, 0) > 0:
            money += p
            inventory[s] -= 1

    print("{:.0f}".format(round(money)))
