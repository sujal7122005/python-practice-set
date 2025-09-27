'''
Delete set of keys from Python Dictionary.
'''
dict_data = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
keys_to_delete = ['b', 'd']
for key in keys_to_delete:
    dict_data.pop(key, None) 
print("Dictionary after deletion:", dict_data) 