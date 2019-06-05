'''
Write a program which reads a rectangle and a circle, and determines whether the circle is arranged inside the rectangle. 
As shown in the following figures, the upper right coordinate (W,H) of the rectangle and the central coordinate x,y) and 
radius r of the circle are given.
Input Five integers W, H, x, y and r separated by a single space are given in a line.
Output Print "Yes" if the circle is placed inside the rectangle, otherwise "No" in a line.
'''
x = input().split()
W, H, x, y, r = int(x[0]), int(x[1]), int(x[2]), int(x[3]), int(x[4])

if r <= x and r <= y and x + r <= W and y + r <= H:
    print('Yes')
else:
    print('No')