def numbers(n, m):
    if n in m:
        return True
    else:
        return False


x = [j for j in input().split(',')]
y = input()
print(numbers(y, x))
