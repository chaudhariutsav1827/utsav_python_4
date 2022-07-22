print("\nword count".title())
s=input('Enter string:')
b = 0
for i in range(len(s)):
    if s[i] == " " and s[i + 1] != " ":
        b += 1
print(b+1)

