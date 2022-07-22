# Write a Python program to remove duplicates from a list.
s=input('Enter list of string as a sentence:')
l=s.split(' ')
print(l)
b=0
for i in l:
    c=l.count(i)
    while c>1:
        for j in range(b+1,len(l)):
            if l[j]==i:
                l.pop(j)
                c-=1
                break
    b+=1
print('After removing duplicates:')
print(l)
