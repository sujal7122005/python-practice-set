'''
Given a list of numbers, return true if first and last number of a list is same.
'''
list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input(f"Enter number {i + 1}: ".format(i + 1)))
    list1.append(num)
if(list1[0] == list1[-1]):
    print("First and last number are the same.")
else:
    print("First and last number are not the same.")