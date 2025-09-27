'''
Given a list iterate it and count theoccurrence of each element and create a dictionary to
show the count of each element.
'''
lst = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
count_dict = {}
for item in lst:
    if item in count_dict:
        count_dict[item] += 1
    else:
        count_dict[item] = 1
print("Count of each element:", count_dict)