""
# Exercise 5: Take the following Python code that stores a string:
# str = 'X-DSPAM-Confidence:0.8475'
# Use find and string slicing to extract the portion of the string after the
# colon character and then use the float function to convert the extracted
# string into a floating point number.
""
s = 'X-DSPAM-Confidence:0.8475'
i = s.find(':')
v = s[i+1:]
fv = float(v)
print(fv)