def number_list(number_data, x):
    for i in number_data:
        if x == i:
            return True
    return False
print(number_list([1, 5, 8, 3], 3))
print(number_list([1, 5, 8, 3], -1))