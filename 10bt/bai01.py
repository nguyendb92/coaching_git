def biggest_number(b):
    """
    # find the Max of three numbers
    Args:
        input_data(list):
    Returns:
        _type_: int
    """
    return max(b)


if __name__ == "__main__":
    lst = [int(y) for y in input().split()]
    print(biggest_number(lst))
