'''
Write a Python program to create and display all combinations of letters,
selecting each letter from a different key in a dictionary.
'''
d = {'1': ['a', 'b'], '2': ['c', 'd']}
l1 = list(d.keys())
l2 = list(d.values())
for i in range(len(l2)-1):
    for j in range(len(l2[i])):
        print(l2[i][i]+l2[i+1][j])
        print(l2[i][i+1]+l2[i+1][j])
            
