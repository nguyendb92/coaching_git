def factorial(n):
    """
    # calculate the factorial of a number
    Args:
        input_data(int):
    Returns:
        _type_:int
    """
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


if __name__ == "__main__":
    x = int(input())
    print(factorial(x))
