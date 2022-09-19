def Multiply(numbers):
    y = 1
    for x in numbers:
        y *= x
    return y


Lst = [int(j) for j in input().split()]
print(Multiply(Lst))
