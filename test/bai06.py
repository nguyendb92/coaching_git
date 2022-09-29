def Print(n):
    for i in n:
        if int(i) == 237:
            break
        elif int(i) % 2 == 0:
            print(i)


x = [j for j in input().split(", ")]
print(Print(x))
