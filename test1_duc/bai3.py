def color(list):
    return list[0], list[-1]


x = [j for j in input().split(",")]
print(color(x))
