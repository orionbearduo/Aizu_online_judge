'''
Write a program which prints small/large/equal relation of given two integers a and b.
Input Two integers a and b separated by a single space are given in a line.
Output a < b, a > b or a = b
'''
a,b=map(int, input().split())
if a < b:
    print("a < b")
elif a == b:
    print("a == b")
else:
    print("a > b")
