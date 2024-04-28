intersection = lambda list1, list2: [value for value in list1 if value in list2]

list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
result = intersection(list1, list2)
print("Intersection of lists:", result)