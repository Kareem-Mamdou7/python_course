string = "***"
for i in range(1, 6):
    print((string * (6 - i)).rjust(15, " "))

print()

for i in range(1, 6):
    print((string * i).ljust(15, " "))

print()

starNumber = 1

for i in range(1, 6):
    print(("*" * starNumber).center(15, " "))
    starNumber += 2
