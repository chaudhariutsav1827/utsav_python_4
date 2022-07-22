print("Swap numbers with temp variable".center(40, '*'))
a = input("Enter the value of A:")
b = input("Enter the value of B:")
c = a
a = b
b = c
print("A:", a, "B:", b)
print("Swap numbers without temp variable".center(40, '*'))
a, b = b, a
print("A:", a, "B:", b)
