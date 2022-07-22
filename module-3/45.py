'''
 Write a Python program to print all unique values in a dictionary.
'''
d1 = {'a': 100, 'b': 200, 'c':300,'d':400,'e':200,'f':100,'g':300}
print(d1)
l=list(d1.values())
l2=[]
for i in l:
    if i not in l2:
        l2.append(i)
print('Unique values'.center(20,'*'))
print(l2)
