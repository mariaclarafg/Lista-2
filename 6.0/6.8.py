def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string


original_string = "maria"
reversed_string = reverse_string(original_string)
print("Original string:", original_string)
print("Reversed string:", reversed_string)