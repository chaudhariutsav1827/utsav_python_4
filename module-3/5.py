# Write a Python function to get the largest number, smallest num and sum 
of all from a list.
l=[23,56,45,32,65,87,12,34,43,76,21]
smallest=max=l[0]
sum=0
for i in l:
    if i>max: 
        max=i
    if smallest>i:
        smallest=i
    sum+=i
print('smallest:',smallest,'\nlargest:',max,'\nsum:',sum)
