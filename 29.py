'''
Given a two list. Create a third list by picking an odd-index element from thefirst list
and even index elements from second.
'''
list1 = [1, 2, 3, 4, 5, 6]
list2 = [10, 20, 30, 40, 50, 60]
list3 = []
for i in range(len(list1)):
    if i % 2 != 0:  # Odd index from list1
        list3.append(list1[i])

for i in range(len(list2)):
    if i % 2 == 0:  # Even index from list2
        list3.append(list2[i])
print("Third list:", list3)