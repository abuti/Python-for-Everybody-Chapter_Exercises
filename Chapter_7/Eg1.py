# fname = input("Enter a file name: ")
fhand = open("mbox-short.txt")
c = 0
for line in fhand:
    c = c + 1
    line = line.rstrip()
    if line.startswith("From"):
        print(line)
print(c)
# print(len(fhand.read()))