'''
How to check file is empty or not.
'''
with open('18.py', 'r') as file:
    content = file.read()
    if content != 0:  # Check if the content is empty or contains only whitespace
        print("The file is not  empty.")
    else:
        print("The file is  empty.")