'''
Write a Python script to check if a given key already exists in a dictionary.

'''
cityCode={'Ahmedabad':79, 'Mumbai':22,'Pune':20,'Delhi':11}
a=input('Enter key: ')
for i in cityCode.keys():
    if i==a:
        print('Key exist in the dictionary')
        break
else:
        print('Key doesn\'t exist in the dictionary')
