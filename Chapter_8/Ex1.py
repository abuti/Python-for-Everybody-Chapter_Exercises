""
# Exercise 1: Write a function called chop that takes a list and modifies
# it, removing the first and last elements, and returns None. Then write
# a function called middle that takes a list and returns a new list that
# contains all but the first and last elements.
""
def chop(a):
    del a[0]
    del a[len(a) - 1]
def middle(a):
    b = a[1:(len(a) - 1)]
    return b
c = [1,3, 5, 7, 9, 11, 13, 15, 17, 19]
d = chop(c)
e = middle(c)

print(c)
print(d)
print(e)