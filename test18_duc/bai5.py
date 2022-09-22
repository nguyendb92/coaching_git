def factorinal(x):
    res = 1
    for i in range(2, x + 1):
        res *= i
    return res


x = int(input())
print(factorinal(x))
