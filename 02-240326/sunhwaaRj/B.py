N = int(input())
lst = list(map(int, input().split()))
cal = list(map(int, input().split()))

minval = 1e9
maxval = -1e9

def dfs(n, temp) :
    global minval, maxval
    
    # 종료 조건
    if n == N-1:
        maxval = max(temp, maxval)
        minval = min(temp, minval)
        return
    
    # 덧셈
    if (cal[0] != 0):
        cal[0] -= 1
        dfs(n+1, temp + lst[n+1])
        cal[0] += 1
        
    # 뺄셈
    if (cal[1] != 0):
        cal[1] -= 1
        dfs(n+1, temp - lst[n+1])
        cal[1] += 1
        
    # 곱셈
    if (cal[2] != 0):
        cal[2] -= 1
        dfs(n+1, temp * lst[n+1])
        cal[2] += 1
        
    # 나눗셈
    if (cal[3] != 0):
        cal[3] -= 1
        dfs(n+1, int(temp / lst[n+1]))
        cal[3] += 1

dfs(0, lst[0])
print(maxval)
print(minval)