""
# Exercise 1: Write a while loop that starts at the last character in the
# string and works its way backwards to the first character in the string,
# printing each letter on a separate line, except backwards.
""
s = "banana"
l = len(s) - 1
while l >= 0:
    print(s[l])
    l = l - 1
print(s[:])

