def even_or_odd(n):
    """
    # find even and odd numbers
    Args:
        input_data(int):
    Returns:
        _type_:str
    """
    if n % 2 == 0:
        return 'even'
    else:
        return 'odd'


def numbers(b):
    """
    # returns a list of 'even' and 'odd'
    Args:
        input_data(list):
    Returns:
        _type_: list
    """
    x = [even_or_odd(i) for i in b]
    return x


if __name__ == "__main__":
    a = int(input())
    y = [j for j in range(a)]
    print(numbers(y))
