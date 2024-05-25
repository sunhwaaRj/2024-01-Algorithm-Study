# BOJ 15655

N, M = map(int, input().split())

A = list(map(int, input().split()))

A.sort()
num = []

def dfs(n):
    if len(num) == M:
        print(*num)
        return
    for i in range(n, len(A)):
        if not A[i] in num:
            num.append(A[i])
            dfs(i+1)
            num.pop()
            
dfs(0)
        