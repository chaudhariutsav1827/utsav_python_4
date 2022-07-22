'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
'''
d = {'1': ['a', 'b'], '2': ['c', 'd']}
l = list(d.values())
for i in range(len(l)-1):
    for j in range(len(l[i])):
        for k in range(i+1, len(l)):
            for l in range(len(l[k])):
                print(l[i][j])
                print(l[k][l])
   
