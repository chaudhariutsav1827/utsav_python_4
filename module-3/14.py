'''
Write a Python program to select an item randomly from a list.

'''
import random
l=[]
for i in range(1,101):
    l.append(i)
item=random.choice(l)
print(item)
