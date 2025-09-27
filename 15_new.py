'''
Given a list of numbers, iterate it and print only those numbers which are divisible of 5.
'''
list1 = []
n = int(input("Enter the number of elements in the list: "))
for i in range(n):
    num = int(input(f"Enter number {i + 1}: ".format(i + 1)))
    list1.append(num)

for i in list1:
    if i % 5 == 0:
        print(i, "is divisible by 5.")
        list2.append(i)
    else:
        print(i, "is not divisible by 5.")

print("Numbers divisible by 5 in the list:", list2)