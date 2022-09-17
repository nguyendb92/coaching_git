x = input()
y = x.split(",")
for i in y:
    if i == 237:
        break
    elif i % 2 == 0:
        print(i)
