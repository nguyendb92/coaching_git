def multiply(*lst):
    res = 1
    for x in lst:
        res *= x
    return res


if __name__ == '__main__':
    print(multiply(12, 24, 45, 67, 67))
