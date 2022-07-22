"""
Write a Python program to find the highest 3 values in a dictionary
"""
d = {'a': 800, 'b': 200, 'c': 500, 'd': 400, 'e': 700, 'f': 100}
l1 = list(d.values())
print(l1)
a = max(l1)
b = min(l1)
for i in l1:
    if i > b and i < a:
        b = i
c = min(l1)
for i in l1:
    if i > c and i < b:
        c = i
print('Highest:        ', a)
print('Second highest: ', b)
print('Third highest:  ', c)

