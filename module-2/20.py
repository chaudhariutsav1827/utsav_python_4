s=input('Enter list of words as a sentence:')
l=s.split(' ')
max=0
for i in l:
    if len(i)>max:
        max=len(i)
print(max)
