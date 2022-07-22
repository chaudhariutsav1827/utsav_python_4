'''
Write a Python program to find the repeated items of a tuple.
'''
t=('apple','bannana','pineapple','orange','potato','apple','bannana','tomato','tomato','onion','brocolli')
l=[]
for i in t:
    if t.count(i)>1 and i not in l:
        l.append(i)
print(l)
