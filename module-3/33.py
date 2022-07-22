'''
Write a Python script to sort (ascending and descending) a dictionary by 
value.

'''
t=((1,2),(3,10),(5,6),(7,8),(9,4))
dic=dict(t)
print(dic)
print(dic.values())
l=list(dic.values())
l.sort()
print('Ascending:',l)
l.reverse()
print('Descendind:',l)

