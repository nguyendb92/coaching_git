def vitri(y):
    b = [(y.index(a), a) for a in y]
    return b


x = [j for j in input().split(', ')]
print(vitri(x))
