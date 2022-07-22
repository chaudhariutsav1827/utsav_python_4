s = 'w3resource'
print(s)
l = []
for i in range(len(s)):
    l.append(s[i])
print(l)
c = []
d = []
e = []
b = 0
for i in l:
    s = l.count(i)
    if i not in d and s > 1:
        c.append(s)
        d.append(i)
    elif s == 1:
        c.append(s)
    else:
        e.append(b)
    b += 1
b = 0
for i in range(len(e)):
    l.pop(e[i]-b)
    b += 1
x = zip(l, c)
print(dict(x))
