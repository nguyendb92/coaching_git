def so_cong(number):
    res = 0
    for i in number:
        res += i
    return res


if __name__ == '__main__':
    print(so_cong((1, 67, 890, 234, 556)))
