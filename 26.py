'''
Given 2 strings, s1 and s2, create a newstring by appending s2 in the middle ofs1.
'''
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
def append_in_middle(s1, s2):
    mid_index = len(s1) // 2
    return (s1[:mid_index] + s2 + s1[mid_index:])
result = append_in_middle(s1, s2)
print(result)