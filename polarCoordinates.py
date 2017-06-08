#!/bin/env python3
"""

https://www.hackerrank.com/challenges/polar-coordinates

Task: convert complex number to polar coordinates
INPUT: z
OUTPUT: 2 lines
 value of r
 value of phi

z is a complex number where z = x + yj, where j is imaginary unit
polar coordinate (r, phi),
 where modulus r is equivalent to distance from z to origin,
 r = sqrt ( x**2 + y**2 )
 where phi counter clockwise angle measured from the positive x-axis
 to the line segment that joins z to the origin.

"""
import cmath


z = complex(input())
r = abs(z)
print(r)
phi = cmath.phase(z)
print(phi)
