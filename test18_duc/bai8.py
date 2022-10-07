def return_b(x):
    b = [(x.index(a), a) for a in x]
    return b


if __name__ == '__main__':
    print(return_b())
