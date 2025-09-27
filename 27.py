'''
Given 2 strings, s1, and s2 return a newstring made of the first, middle and lastchar each
input string.
'''
s1 = input("Enter the first string: ")
s2 = input("Enter the second string: ")
def first_middle_last(s1, s2):
    if len(s1) < 3 or len(s2) < 3:
        return "Both strings must be at least 3 characters long"
    first_s1 = s1[0]
    a = len(s1) // 2
    if len(s1) % 2 == 0:
        middle_s1 = s1[a - 1:a + 1]
    middle_s1 = s1[a]
    last_s1 = s1[-1]
    
    first_s2 = s2[0]
    b = len(s2) // 2
    if len(s2) % 2 == 0:    
        middle_s2 = s2[b - 1:b + 1]
    middle_s2 = s2[b]
    last_s2 = s2[-1]
    
    return first_s1 + middle_s1 + last_s1 + first_s2 + middle_s2 + last_s2
result = first_middle_last(s1, s2)
print(result)