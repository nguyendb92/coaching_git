x = input()
y = x.split(",")
a = int(input())
b = False
for i in y:
    if a == i:
        b = True
print(b)
