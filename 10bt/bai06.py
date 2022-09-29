def divisible_by_7(x):
    """
    # find numbers divisible by 7
    Args:
        input_data(list):
    Returns:
        _type_:list
    """
    a = [j for j in range(x[0], x[-1] + 1) if j % 7 == 0]
    return a


if __name__ == "__main__":
    m = [int(n) for n in input().split()]
    print(divisible_by_7(m))
