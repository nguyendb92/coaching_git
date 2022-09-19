def Sum(numbers):
    y = 0
    for x in numbers:
        y += x
    return y


Lst = [int(j) for j in input().split()]
print(Sum(Lst))
