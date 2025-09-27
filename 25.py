'''
Given a string of odd length greater 7, return a string made of the middle threechars of a
given String.
'''
s = input("Enter a string of odd length greater than 7: ")
def middle_three_chars(s):
    if len(s) > 7:
        mid_index = int(len(s) / 2)
        return s[(mid_index - 1):(mid_index + 2)]
    else:
        return "String must be of odd length greater than 7"
a = middle_three_chars(s)
print(a)