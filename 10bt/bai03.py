def multiply_list(number_list):
    """
    # multiply all the numbers in a list
    Args:
        input_data(list):
    Returns:
        _type_:int
    """
    y = 1
    for x in number_list:
        y *= x
    return y


if __name__ == "__main__":
    lst = [int(j) for j in input().split()]
    print(multiply_list(lst))
