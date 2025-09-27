'''
Given a range of first 10 numbers, Iterate from start number to the end number and
print the sum of the current number and previous number.
'''
num1 = 0
num2 = 10
for i in range(num1, num2):
    if i == 0:
        print("Current number:", i, "Previous number: None")
    else:
        print("Current number:", i, "Previous number:", i - 1, "Sum:", i + (i - 1))
