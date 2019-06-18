"""
Official House
You manage 4 buildings, each of which has 3 floors, each of which consists of 10 rooms.
Write a program which reads a sequence of tenant/leaver notices, and reports the number of tenants for each room.

For each notice, you are given four integers b, f, r and v which represent
that v persons entered to room r of fth floor at building b. If v is negative, it means that −v persons left.

Assume that initially no person lives in the building.

Input
In the first line, the number of notices n is given. In the following n lines,
a set of four integers b, f, r and v which represents ith notice is given in a line.

Output
For each building, print the information of 1st, 2nd and 3rd floor in this order. For each floor information,
print the number of tenants of 1st, 2nd, .. and 10th room in this order.
Print a single space character before the number of tenants. Print "####################" (20 '#') between buildings.

"""
room = [[[],[],[]],[[],[],[]],[[],[],[]],[[],[],[]]]
for i in range(4):
    for j in range(3):
        for k in range(10):
            room[i][j].append(0)
n = int(input())
for _ in range(n):
    b, f, r, v = map(int, input().split())
    room[b-1][f-1][r-1] += v

for i in range(4):
    for j in range(3):
        print(" "+" ".join(map(str, room[i][j])))
    if i != 3: print("#"*20)
