def list(n):
    x = n.split(',')
    return x


def Tuple(i):
    y = tuple(list(i))
    return y


b = input()
print(list(b))
print(Tuple(b))