def ReduceFraction(a, b):
    Z1 = max(a, b)
    Z2 = min(a, b)
    if Z1 == Z2 and Z1 * Z2 != 0:
        return 1, 1
    else:
        Z = Z1 % Z2
        while Z > 0:
            Z1 = Z2
            Z2 = Z
            Z = Z1 % Z2
        return a // Z2, b // Z2
a = int(input())
b = int(input())
print(*ReduceFraction(a, b))
