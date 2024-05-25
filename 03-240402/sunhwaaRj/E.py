# BOJ 5904

# 분할정복
N = int(input())

def recursive(total_length, mid_length, N):
    if N <= 3:
        return "moo"[N-1]

    left_length = (total_length - mid_length) // 2

    if N <= left_length:
        return recursive(left_length, mid_length - 1, N)

    if N > left_length + mid_length:
        return recursive(left_length, mid_length - 1, N - left_length - mid_length)

    if N - left_length == 1:
        return "m"
    else:
        return "o"


total_length = 3  
n = 0  
while total_length < N:
    n += 1
    total_length = 2 * total_length + n + 3

print(recursive(total_length, n+3, N))