def factorinal(x):
    res = 1
    for i in range(2, x + 1):
        res *= i
    return res


if __name__ == '__main__':
    print(factorinal(12))
