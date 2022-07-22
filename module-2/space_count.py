s = "My  name  is   Utsav."
b = 0
print("Space count".title())
for i in range(0, len(s)):
    if s[i] == " ":
        b += 1
print(b)

