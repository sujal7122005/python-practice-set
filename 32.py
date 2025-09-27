'''
Iterate a given list and Check if a given element already exists in a dictionary as a key’s
value if not delete it from the list.
'''
lst = [1, 2, 3, 4, 5, 6]
my_dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
filtered_list = [item for item in lst if item in my_dict]
print("Filtered list:", filtered_list)