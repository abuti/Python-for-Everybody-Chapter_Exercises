""
# Exercise 6: Rewrite your pay computation with time-and-a-half for overtime 
# and create a function called computepay which takes two parameters (hours and rate).
# Enter Hours: 45
# Enter Rate: 10
# Pay: 475.0
""

def computepay(hrs, rate):
    gp = 0
    if hrs > 40:
        gp = (rate * 40) + (rate * (hrs - 40) * 1.5)
    else:
        gp = hrs * rate
    return gp
try:
    hrs = float(input("Enter amount of hours done: "))
    rate = float(input("Enter the rate: "))
except:
    print("Error, please enter numeric input")
print("Gross_pay = ", computepay(hrs, rate))