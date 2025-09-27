'''
Given a two integer numbers return their product and if the product is greater than
1000, then return their sum.
'''
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = num1 * num2
if num3 > 1000:
    print("Sum:", num1 + num2)
else:
    print("Product:", num3)
