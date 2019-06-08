"""
Write a program which reads two integers x and y, and prints them in ascending order.

Input
The input consists of multiple datasets. Each dataset consists of two integers x and y separated by a single space.

The input ends with two 0 (when both x and y are zero). Your program should not process for these terminal symbols.

Output
For each dataset, print x and y in ascending order in a line. Put a single space between x and y.
"""
while True:
    x, y = map(int, input().split())
    if x == 0 and y == 0:
        break
    if x > y:
        x, y = y, x
    print("%d %d" % (x, y))
