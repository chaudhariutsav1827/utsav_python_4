''' Write a Python program to count the number of strings where the string 
length is 2 or more and the first and last character are same from a given 
list of strings.'''

s=input('Enter list of string as a sentence:')
l=s.split(' ')
count=0
for i in l:
    if len(i)>=2 and i[0]==i[len(i)-1]:
        print(i)
        count+=1
print('count:'count)
