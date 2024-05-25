# BOJ 2229

n = int(input())

students = list(map(int, input().split()))
g = [0 for _ in range(1+n)]

for i in range(n+1):
    max_score = 0
    min_score = 10001
    for j in range(i, 0, -1):
        max_score = max(max_score, students[j-1])
        min_score = min(min_score, students[j-1])
        g[i] = max(g[i], max_score - min_score + g[j-1])

print(g[n])