"""
Print a Frame
Draw a frame which has a height of H cm and a width of W cm. For example, the following figure shows a frame which
has a height of 6 cm and a width of 10 cm.

##########
#........#
#........#
#........#
#........#
##########
Input
The input consists of multiple datasets. Each dataset consists of two integers H and W separated by a single space.

The input ends with two 0 (when both H and W are zero).

Output
For each dataset, print the frame made of '#' and '.'.

Print a blank line after each dataset.
"""
while True:
    W, H = map(int, input().split())

    if W == 0 and H == 0:
        break
    for i in range(H):
        for k in range(W):
            if i == 0 or i == H - 1 or k == 0 or k == W - 1:
                print('#', end="")
            else:
                print('.', end="")
        print()
    print()
