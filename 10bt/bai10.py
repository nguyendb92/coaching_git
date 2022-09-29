def common(a, b):
    """
    # Find the common numbers in two lists
    Args:
        input_data(list):
    Returns:
        _type_:list
    """
    z = [i for i in a if i in b]
    return z


if __name__ == "__main__":
    list_1 = [int(j) for j in input().split()]
    list_2 = [int(z) for z in input().split()]
    print(common(list_1, list_2))
