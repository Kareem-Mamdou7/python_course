user = input("Enter your name: ")
print(f"Welcome!, {user}")

a = int(input("Enter a: "))  # will be int always even if entered a float
b = int(input("Enter b: "))
print(f"a is {a}")
print(f"b is {b}")
print(f"Sum of a and b is {a+b}")

a = "Hello,\n World"  # Goes to new line
print(a)

a = "Hello,\\ World"  # prints the "\"
print(a)

a = "Hello,' World"  # prints the single quote
print(a)

a = "Hello,\t World"  # adds tab space
print(a)
