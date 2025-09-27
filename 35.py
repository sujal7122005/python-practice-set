'''
Convert two lists into the dictionary and merge two Python dictionaries into one.
'''
list1 = ['a', 'b', 'c']
list2 = [1, 2, 3]
merged_dict = dict(zip(list1, list2))
print("Merged dictionary:", merged_dict)
