readline = open(0).readline
N, M = map(int, readline().split())
A = [list(map(int, readline().split())) for i in range(N)]
B = [int(readline()) for i in range(M)]
print(*map((lambda Ai: sum(a*b for a, b in zip(Ai, B))), A), sep='\n')

"""
n, m = list(map(int, input().split()))
a = []
for i in range(n):
  a.append([int(j) for j in input().split()])
b = []
for i in range(m):
  b.append(int(input()))
for i in range(n):
  s = 0
  for j in range(m):
    s += a[i][j] * b[j]
  print(s)
"""
