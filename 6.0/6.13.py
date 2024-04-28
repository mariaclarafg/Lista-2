def filter_list(original_list, func):
    return [item for item in original_list if func(item)]


original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def is_even (x):
    if lambda x: x % 2 == 0:
        return True

filtered_list = filter_list(original_list, is_even)
print("Filtered list:", filtered_list)