# BOJ 10986

N, M = map(int, input().split())
A = list(map(int, input().split()))

r =  [0] * M
sum = 0

for i in range(N):
    sum += A[i]
    r[sum % M] += 1

ans = r[0] # 나머지가 0이 되는 경우의 수
for i in range(M):
    ans += r[i] * (r[i] - 1) // 2
    
print(ans)
