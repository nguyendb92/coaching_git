def common(a, b):
    z = [i for i in a if i in b]
    return z


x = [int(j) for j in input().split()]
y = [int(z) for z in input().split()]
print(common(x, y))
