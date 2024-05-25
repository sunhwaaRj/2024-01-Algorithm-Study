t = int(input())
res = []

for _ in range(t):
    n = int(input())
    phonebook = []
    for _ in range(n):
        phonebook.append(input())
    phonebook.sort() # 사전 순 정렬
    for i in range(n - 1):
        if phonebook[i] == phonebook[i + 1][:len(phonebook[i])]:
            res.append('NO')
            break
    else: res.append('YES')

for result in res: # 결과
    print(result)