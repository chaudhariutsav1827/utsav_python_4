'''
Write a Python program to find the second smallest number in a list.
'''
import random
l=[]
for i in range(10):
    l.append(random.randint(1,100))
print(l)
smallest=min(l)
second_smallest=l[0]
for i in l:
    if i>smallest and i<second_smallest:
        second_smallest=i
print('smallest number: ',smallest)
print('second smallest: ',second_smallest)
