def string(str):
    """
    # reverse a string
    Args:
        input_data(str):
    Returns:
        _type_:str
    """
    b = str[::-1]
    return b


if __name__ == "__main__":
    string_a = str(input())
    print(string(string_a))
