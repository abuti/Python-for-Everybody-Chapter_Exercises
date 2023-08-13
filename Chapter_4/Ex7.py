""
# Exercise 7: Rewrite the grade program from the previous chapter using
# a function called computegrade that takes a score as its parameter and
# returns a grade as a string.
# Score Grade
# >= 0.9 A
# >= 0.8 B
# >= 0.7 C
# >= 0.6 D
# < 0.6 F
# Enter score: 0.95
# A
# Enter score: perfect
# Bad score
# Enter score: 10.0
# Bad score
# Enter score: 0.75
# C
# Enter score: 0.5
# F
# Run the program repeatedly to test the various different values for input.
""

def computegrade(s):
    if s >= 0.9 and s < 1.0:
        return "A"
    elif s >= 0.8 and s < 0.9:
        return "B"
    elif s >= 0.7 and s < 0.8:
        return "C"
    elif s >= 0.6 and s < 0.7:
        return "D"
    elif s < 0.6:
        return "F"
    else:
        return "Bad score"

score = input("Enter score: ")
try:
    s = float(score)
except:
    print("Bad score")
    quit()
print("Grade =", computegrade(s))
