def fact(n):
    if (n > 1):
        return n*fact(n-1)
    else:
        return 1
    
n, m = map(int, input().split())

print(fact(n) // (fact(n-m) * fact(m)))