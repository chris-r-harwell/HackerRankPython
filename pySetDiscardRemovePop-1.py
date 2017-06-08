#!/bin/env python3
"""
REF:
 https://www.hackerrank.com/challenges/py-set-discard-remove-pop

 .remove(x)

  operation removes element x from the set.
  returns: None.
  raises KeyError if element x does not exist

 .discard(x)

  liked .remove(x) without KeyError

 .pop(x)
  operation removes and returns an arbitrary element from the set.
  raises KeyError if no elements to remove.

Task:
    You have a non-empty set s, and you have to execute N commands
    given in N lines.
    The commands will be pop, remove, discard.

INPUT:
    lines:
    1 - integer n, number of elements in set s
    2 n space separated elements of set s
      all elements non-negative,  <= 9
    3 - integer N, the number of commands
    4...4+N commands to execute
     pop, remove and/or discard commands followed by their associated
     value.
Constraints:
    0 < n < 20
    0 < N < 20
OUTPUT:
    sum of elements of set s on a single line
"""
if __name__ == '__main__':
    n = int(input().strip())
    s = set(map(int, input().strip().split()))
    for i in range(N = int(input())):
        line = input().strip().split()
        cmd = line[0]
        if cmd == "pop":
            s.pop()
        elif cmd == "remove":
            s.remove(int(line[1]))
        elif cmd == "discard":
            s.discard(int(line[1]))
    print(sum(s))
