'''
Given a string, display only those characters which are present at an evenindex number.
'''
str = input("Enter a string: ")
even_indexed_chars = str[::2]
print("Characters at even index positions:", even_indexed_chars)