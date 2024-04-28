def find_max_value(input_list):
    if not input_list:
        return None  
    else:
        return max(input_list)


my_list = [10, 5, 8, 20, 15]
max_value = find_max_value(my_list)
print("The largest value in the list is:", max_value)