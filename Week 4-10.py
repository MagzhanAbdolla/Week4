def sumOfNum():
    a = int(input())
    if a == 0:
        return 0
    return a + sumOfNum() - 1
print(sumOfNum())
