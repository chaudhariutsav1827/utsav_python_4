l=[1,2,3,4,(),(),(3,6,2),(1,3),(),(8,7),()]
print(l)
while(l.count(())>0):
    for i in l:
        if i==():
            l.remove(i)
            break
print(l)
