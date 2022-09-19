def divisible_by_7(x):
    a = [j for j in range(x[0], x[-1] + 1) if j % 7 == 0]
    return a


m = [int(n) for n in input().split()]
print(divisible_by_7(m))
