s=input('Enter the string:')
a=s.find('not')
b=s.find('poor',a)
if a!=-1 and b!=-1:
    print(s[:a]+'good'+s[b+4:])

