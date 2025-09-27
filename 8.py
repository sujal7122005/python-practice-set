'''
Reverse a given number and return true if it is the same as the original number.
'''
num = int(input("Enter a number: "))
reverse_num = int(str(num)[::-1])
if num == reverse_num:
    print("The number is a palindrome.")
else:
    print("The number is not a palindrome.")
    