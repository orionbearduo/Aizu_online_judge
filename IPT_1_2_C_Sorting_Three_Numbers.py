'''
Write a program which reads three integers, and prints them in ascending order.
Input Three integers separated by a single space are given in a line.
Output Print the given integers in ascending order in a line. Put a single space between two integers.
Sample Input 1:  3 8 1
Sample Output 1: 1 3 8
'''
sortingThreeNum = list(map(int, input().split()))
sortingThreeNum.sort()
print(sortingThreeNum[0], sortingThreeNum[1], sortingThreeNum[2])

'''
a = input().split()
print(" ".join(sorted(a)))
'''