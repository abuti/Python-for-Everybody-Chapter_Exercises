""
# Exercise 1: Run the program on your system and see what numbers
# you get. Run the program more than once and see what numbers you get.
# The random function is only one of many functions that handle random numbers.
# The function randint takes the parameters low and high, and returns an integer
# between low and high (including both).
""
import random as r

print(r.randint(1, 10))
print(r.randint(1, 10))
t = [1, 3, 5, 7, 9]
print(r.choice(t))