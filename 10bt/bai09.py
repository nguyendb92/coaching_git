def even_or_odd(n):
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'


def numbers(b):
    x = [even_or_odd(i) for i in b]
    return x


a = int(input())
y = [j for j in range(a)]
print(numbers(y))
