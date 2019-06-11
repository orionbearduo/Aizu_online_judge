"""
Print a Chessboard
Draw a chessboard which has a height of H cm and a width of W cm. For example, the following figure shows a chessboard which has a height of 6 cm and a width of 10 cm.

#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
#.#.#.#.#.
.#.#.#.#.#
Note that the top left corner should be drawn by '#'.

Input
The input consists of multiple datasets. Each dataset consists of two integers H and W separated by a single space.

The input ends with two 0 (when both H and W are zero).

Output
For each dataset, print the chessboard made of '#' and '.'.

Print a blank line after each dataset.
"""
while True:
	H, W = map(int, input().split())
	if H == 0 and W == 0:
		break
	for i in range(H):
		for j in range(W):
			if (i + j) % 2 == 0:
				print("#", end = '')
			else:
				print(".", end = '')
		print()
	print()
