"""
Write a program which calculates the area and perimeter of a given rectangle.

*Input
The length a and breadth b of the rectangle are given in a line separated by a single space.

*Output
Print the area and perimeter of the rectangle in a line. The two integers should be separated by a single space.

Constraints
1 ≤ a, b ≤ 100

Sample Input 1
3 5
Sample Output 1
15 16
"""
# Solution
a, b = map(int, input().split())
print(a*b, 2*(a+b))
