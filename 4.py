'''
Given a string and an integer number n,remove characters from a string starting from
zero up to n and return a new string.
'''
str = input("Enter a string: ")
n = int(input("Enter an integer number: "))
new_str = str[n:]
print("New string after removing characters:", new_str)
