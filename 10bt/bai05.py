def gt(n):
    if n == 1:
        return 1
    else:
        return n * gt(n - 1)


x = int(input())
print(gt(x))
