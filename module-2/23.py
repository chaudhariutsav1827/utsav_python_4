print(' Write a Python function to insert a string in the middle of a string.')
s = input('Enter the string:')
s1 = input('Enter another string:')
a = int(len(s) / 2)
print(s[0:a] + s1 + s[(a + 1):])