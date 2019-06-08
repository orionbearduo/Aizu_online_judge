"""
Write a program which reads three integers a, b and c, and prints the number of divisors of c between a and b.

Input
Three integers a, b and c are given in a line separated by a single space.

Output
Print the number of divisors in a line.
Sample Input 1
5 14 80
Sample Output 1
3
"""
a, b, c = map(int, input().split())
ans = 0
for i in range(a, b + 1):
    if c % i == 0:
        ans = ans + 1
print(ans)
