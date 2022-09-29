def find_3(x):
    """
    # find numbers with 3 in them
    Args:
        input_data(list):
    Returns:
        _type_: list
    """
    a = [j for j in range(x[0], x[-1] + 1) if '3' in str(j)]
    return a


if __name__ == "__main__":
    m = [int(n) for n in input().split()]
    print(find_3())
