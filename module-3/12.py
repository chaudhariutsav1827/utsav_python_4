'''
Write a Python function that takes a list and returns a new list with unique 
elements of the first list.
'''
l=[1,2,3,2,3,4,5,1,6,7,8]
def unique(l):
    u=[]
    for i in l:
        if i not in u:
            u.append(i)
    print(u)
unique(l)
