"""
Write a program which reads two integers x and y, and prints them in ascending order.

Input
The input consists of multiple datasets. Each dataset consists of two integers x and y separated by a single space.

The input ends with two 0 (when both x and y are zero). Your program should not process for these terminal symbols.

Output
For each dataset, print x and y in ascending order in a line. Put a single space between x and y.
Sample Input
3 2
2 2
5 3
0 0
Sample Output
2 3
2 2
3 5
"""
while True:
    a, b = map(int, input().split())
    if a == b == 0:
        break
    if a <= b:
        print("%d %d" % (a, b))
    else:
        print("%d %d" % (b, a))
