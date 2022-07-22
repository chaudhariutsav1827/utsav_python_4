print('write a python program to sum of three integers if two are equal than sum is zero')
l = []
for i in range(0, 3):
    print('Enter ', i, ':', end='')
    l.append(int(input()))
s = 0
for i in range(2):
    for j in range(i+1, 3):
        if l[i] == l[j]:
            s += 0
        else:
            s += l[i] + l[j]
print(s)
