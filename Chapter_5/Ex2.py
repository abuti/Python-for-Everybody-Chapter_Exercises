""
# Exercise 2: Write another program that prompts for a list of numbers
# as above and at the end prints out both the maximum and minimum of
# the numbers instead of the average.
""

t = 0
c = 0
mn = None
mx = None
while(True):
    n = input("Enter a number:")
    try:
        if n == 'done':
            print(t, c, mn, mx)
            break
        n = int(n)
        t = t + n
        c = c + 1
        if mn is None or n < mn:
            mn = n
        if mx is None or n > mx:
            mx = n
    except:
        print("Invalid input")