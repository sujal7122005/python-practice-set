'''
Given a two list of equal size create a set such that it shows the element fromboth lists in
the pair.
'''
list1 = [1, 2, 3, 4, 5]
list2 = ['a', 'b', 'c', 'd', 'e']
result_set = set(zip(list1, list2))
print("Set of pairs:", result_set)