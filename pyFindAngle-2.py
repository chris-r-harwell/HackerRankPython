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


http://www.sparknotes.com/testprep/books/sat2/math2c/chapter9section9.rhtml

"""
import math

# read in the distances for the big triangle
dAB = int(input())
dBC = int(input())

# Find H = dAC using Pythagorean theorem for right triangle
# dAC = math.sqrt(dAB**2 + dBC**2)
dAC = math.hypot(dAB, dBC)
dCM = dAC / 2
# print("dAC = {}".format(dAC))
# print("dCM = {}".format(dCM))

"""
Find angle c, aACB using
 SOH .. sin X = opposite (O) / hypotenuse (H)
 asin (O/H) = angle in radians
 convert radians to degrees with *= 180/pi
"""
aACB = math.asin(dAB / dAC)
# print("aACB = {} radians".format(aACB))
# aACB *= 180/math.pi
# aACB = math.degrees(aACB)
# aACB = round(aACB)
# print("aACB = {} degrees".format(aACB))

"""
Law of Cosines (for any triangle)

c**2 = a**2 + b**2 - 2ab * cos(C)

need: three of four unknowns.

know: dCM, dBC, C

      a = m = dBC,
      b = dCM
      c = ?
      C = dACB

solve for c (a.k.a dBM)

 c = sqrt( a**2 + b**2 - 2ab*cos(C) )

"""
dBM = math.sqrt(dBC**2 + dCM**2 - 2 * dBC * dCM * math.cos(aACB))
# print("c = {}".format(dBM))

"""
Law of Sines (for any triangle)
need:
lengths of two sides and the measure of an angle opposite one of those sides

sin A/a = sin B/b = sin C/c
where A,B,C are angles
and a,b,c are the length of opposite side to each.

(sin phi)/dCM = (sin C)/dBM = (sin M)/dBC

know:
 dBC (from input)
 dCM (from pythagorean theorem)
 dBM (from law of cosines)
 C = aACB (from SOH)

want phi

 sin phi = (sin C) * dCM/dBM
 phi = sin-1 ( (sin C) * dCM/dBM )
"""

phi = math.asin(math.sin(aACB) * dCM / dBM)
phi = math.degrees(phi)
print("{:.0f}".format(round(phi)) + '\u00b0')
