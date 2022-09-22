num = ["even" if n % 2 == 0 else "odd" for n in range(20)]
print(num)
num = []
for n in range(20):
    if n % 2 == 0:
        num.append("even")
    else:
        num.append("odd")
