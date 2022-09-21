def list(n):
    a = n.split(',')
    return a


def Tuple(x):
    y = tuple(list(x))
    return y


b = input()
print(list(b))
print(Tuple(b))
