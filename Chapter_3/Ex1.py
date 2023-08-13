""
# Exercise 1: Rewrite your pay computation to give the employee 1.5
# times the hourly rate for hours worked above 40 hours.
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
""
hrs = float(input("Enter amount of hours done: "))
rate = float(input("Enter the rate: "))
gp = 0
if hrs > 40:
    gp = (rate * 40) + (rate * (hrs - 40) * 1.5)
    print("Gross pay =", gp)
else:
    gp = hrs * rate
    print("Gross pay =", gp)    