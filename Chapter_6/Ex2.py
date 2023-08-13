""
# Exercise 3: Encapsulate this code in a function named count, and 
# generalize it so that it accepts the string and the letter as arguments.
""
def count(s, l):
    count = 0
    for letter in s:
        if l is letter:
            count = count + 1
    return count
s = "Hello world"
print(count(s, 'l'))
print(type(s))
# print(dir(s))             #to show the methods available to any instance of the object
print(s.split())
print(s.upper())
print(s.lower())
print(s.__dir__())