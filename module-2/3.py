n = int(input("Enter value: "))
a, b = 0, 1
print(a, end="")
while b < n:
    print(" ", b, end="")
    a, b = b, a + b
