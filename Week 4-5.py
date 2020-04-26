def IsPrime(n):
    a = 2
    b = 0
    while a <= pow(n, 0.5) and a > 1:
        if n % a == 0:
            b += 1
        a += 1
    return b == 0
n = int(input())
if IsPrime(n):
    print("YES")
else:
    print("NO")
