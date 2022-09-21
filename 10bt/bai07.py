def find(x):
    a = [j for j in range(x[0], x[-1] + 1) if '3' in str(j)]
    return a


m = [int(n) for n in input().split()]
print(find())
