"""
Min, Max and Sum
Write a program which reads a sequence of
n integers , and prints the minimum value, maximum value and sum of the sequence.

Input
In the first line, an integer n is given. In the next line,
n integers are given in a line.

Output
Print the minimum value, maximum value and sum in a line. Put a single space between the values.
"""
n = int(input())
data = list(map(int, input().split()))

vmin = min(data)
vmax = max(data)
vsum = sum(data)

print(vmin, vmax, vsum)