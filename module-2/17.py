print('Write a Python program to get a single string from two given strings,\nseparated by a space and swap the first two characters of each string.')
s1 = input('\nEnter first string:')
s2 = input('\nEnter second string:')
print(s1[1::-1] + s1[2:] + ' ' + s2[1::-1] + s2[2:])
