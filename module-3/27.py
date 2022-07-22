'''
Write a Python program to replace last value of tuples in a list.
'''
t=('apple','bannana','pineapple','orange','potato','tomato','onion','brocolli')
l=list(t)
item=input('Enter element to replace last element in list: ')
l.pop()
l.append(item)
print(l)
