# BOJ 3273

import sys
input = sys.stdin.readline

n = int(input())
num = list(int, input())
x = int(input())

cnt = 0

i = 0
j = len(num) - 1

num.sort()

while i < j:
    temp = num[i] + num[j]
    if temp == x:
        cnt += 1
        i += 1
        j -= 1
    elif temp < x:
        i += 1
    else:
        j -= 1

print(cnt)