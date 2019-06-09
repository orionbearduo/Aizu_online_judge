"""
Write a program which reads two integers a, b and an operator op, and then prints the value of a op b.

The operator op is '+', '-', '*' or '/' (sum, difference, product or quotient).
The division should truncate any fractional part.

Input
The input consists of multiple datasets. Each dataset is given in the following format.

a op b
The input ends with a single '?'. Your program should not process for this terminal symbol.

Output
For each dataset, print the value in a line.
Sample Input 1
1 + 2
56 - 18
13 * 2
100 / 10
27 + 81
0 ? 0
Sample Output 1
3
38
26
10
108
"""
while True:
    table = input().split()

    a = int(table[0])
    op = table[1]
    b = int(table[2])

    if op == '?':
        break

    if op == '+':
        print('%d' % (a + b))
    elif op == '-':
        print('%d' % (a - b))
    elif op == '*':
        print('%d' % (a * b))
    elif op == '/':
        print('%d' % (a / b))
    else:
        print('invalid input')


