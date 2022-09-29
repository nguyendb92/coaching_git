def vitri(y):
    """
    # return Get the index and the value as a tuple for items in the list
    Args:
        input_data(list):
    Returns:
        _type_: list
    """
    b = [(y.index(a), a) for a in y]
    return b


if __name__ == "__main__":
    x = [j for j in input().split(', ')]
    print(vitri(x))
