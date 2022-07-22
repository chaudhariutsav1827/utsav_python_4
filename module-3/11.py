'''
Write a Python program to generate and print a list of first and last 5 
elements where the values are square of numbers between 1 and 30.
'''
l=[]
for i in range (1,31):
    l.append(i*i)
print(l)
print('First five elements:',l[0:5])
print('Last five elements:',l[-1:-6:-1])
    
