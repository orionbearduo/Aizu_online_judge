"""
Reversing Numbers

Write a program which reads a sequence and prints it in the reverse order.

Input
The input is given in the following format:

n
a1 a2 . . . an
n is the size of the sequence and ai is the ith element of the sequence.

Output
Print the reversed sequence in a line. Print a single space character between adjacent elements (Note that your program should not put a space character after the last element).
"""
n = int(input())

table = list(map(int, input().split()))

table.reverse()

print(' '.join(map(str, table)))
