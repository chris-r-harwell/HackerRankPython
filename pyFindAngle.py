#!/bin/env python3
"""
https://www.hackerrank.com/challenges/find-angle

  A
  |\
  | \
  |  \
  |   \
  |    M
  |     \
  |      \
  |       \
  B________C

ABC is a right triangle, 90 deg. at B.
Point M is midpoint of hypotenuse AC.
f
Constraints
 0 < AB <= 100
 0 < BC <= 100
 AB, BC are natural numbers.

INPUT: (2 lines)
 side AB length
 side BC length

OUPUT:
 angle MBC in degrees
 round to nearest int


or better
We can Solve this problem by using a property:
A median on the hypotenuse divides the right angled triangle in two isoceles triangle.
Means AM=BM=CM
So, ∡MBC = ∡MCB
Now find ∡MCB [You can use 'tan' ]

tan = TOA, tan phi = opp/adj
phi = atan(opp/adj)

"""
import math


# read in the distances for the big triangle
dAB = int(input())
dBC = int(input())
phi = math.atan(dAB/dBC)
phi = math.degrees(phi)
print("{:.0f}".format(round(phi)) + '\u00b0')
