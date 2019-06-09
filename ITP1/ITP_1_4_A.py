"""
Write a program which reads two integers a and b, and calculates the following values:

a ÷ b: d (in integer)
remainder of a ÷ b: r (in integer)
a ÷ b: f (in real number)
Input
Two integers a and b are given in a line.

Output
Print d, r and f separated by a space in a line. For f, the output should not contain an absolute error greater than 10**-5.
"""
a, b = map(int, input().split())
print("%d %d %.10f" % (a/b, a%b, a/b))
