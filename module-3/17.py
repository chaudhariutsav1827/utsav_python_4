'''
Write a Python program to get unique values from a list

'''
l=[1,2,3,2,3,4,5,1,6,7,8]
u=[]
for i in l:
    if i not in u:
        u.append(i)
print(u)
