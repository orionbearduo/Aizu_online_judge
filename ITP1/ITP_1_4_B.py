"""
Write a program which calculates the area and circumference of a circle for given radius r.

Input
A real number r is given.

Output
Print the area and circumference of the circle in a line.
Put a single space between them. The output should not contain an absolute error greater than 10**-5.
"""
import math

r = float(input())
print("%.10f %.10f" % (r * r * math.pi, 2.0 * math.pi * r))
