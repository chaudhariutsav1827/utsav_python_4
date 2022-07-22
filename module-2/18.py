print('Write python program to add "ing" at the end of string. If string already ends\nwith "ing" then add "ly". If length is less than 3 then leave it unchanged.')
s = input('Enter the string:')
if len(s) < 3:
    print(s)
elif s.endswith('ing'):
    print(s + 'ly')
else:
    print(s + 'ing')
