def multiply(number):
    res = 1
    for x in number:
        res *= x
    return res


Lst = [int(j) for j in input().split()]
print(multiply(Lst))
