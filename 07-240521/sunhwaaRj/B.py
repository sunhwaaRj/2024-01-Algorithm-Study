# BOJ 1058

import sys
from collections import deque

n = int(sys.stdin.readline())
graph = [list(sys.stdin.readline().strip()) for _ in range(n)]

f = [[0] * n for _ in range(n)]

for k in range(n):
  for i in range(n):
    for j in range(n):
      if i == j:
        continue
      
      if graph[i][j] == 'Y' or (graph[i][k] == 'Y' and graph[k][j] =='Y'):
        f[i][j] = 1

res = 0

for row in f:
  res = max(res,sum(row))
print(res)