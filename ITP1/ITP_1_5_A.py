"""
Print a Rectangle
Draw a rectangle which has a height of H cm and a width of W cm. Draw a 1-cm square by single '#'.

Input
The input consists of multiple datasets. Each dataset consists of two integers H and W separated by a single space.

The input ends with two 0 (when both H and W are zero).

Output
For each dataset, print the rectangle made of H × W '#'.
"""
while True:
    H, W = map(int, input().split())

    if H == 0 and W == 0:
        break
    for i in range(H):
        print('#' * W)
    print()
