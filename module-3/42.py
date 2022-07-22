'''
Write a Python program to combine two dictionary adding values for 
common keys.
'''
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
print(d1)
print(d2)
l1=list(d1.values())
l2=list(d2.values())
a=0
for i in range(len(l1)):
    l1[a]+=l2[a]
    a+=1
l2=d1.keys()
d3=dict(zip(l2,l1))
print('Output'.center(20,'*'))
print(d3)
