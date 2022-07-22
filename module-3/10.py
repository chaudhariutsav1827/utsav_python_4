'''Write a Python function that takes two lists and returns true if they have 
at least one common member.'''

l1=['apple','bannana','mango','orange','papaya','coconut','watermelon','strawberry','pineapple']
l2=['cabbage','onion','potato','broccoli','carrot','corn','mushroom','cauliflower','garlic']
def common(l1,l2):
    for i in l1:
        if i in l2:
            return True
print(common(l1,l2))
