'''
Find all occurrences of “USA” in givenstring ignoring the case.
'''
str = input("Enter a string: ")
def find_usa_occurrences(s):
    if 'USA'in str.upper():
        return str.upper().count('USA')
    else:
        return "No occurrences of 'USA' found"
result = find_usa_occurrences(str)
print(f"Occurrences of 'USA': {result}")