'''
Read line number 4 from the given file.
'''
with open('6.py', 'r') as file:
    lines = file.readlines()
    if len(lines) > 4:  # Check if there are at least 5 lines
        print(lines[4].strip())  # Print line number 5 (index 4)
    else:
        print("The file does not have enough lines.")