# There's two types of functions in Python:
# 1- Built-in functions: functions that are already defined in Python. Like print().
# 2- User-defined functions: functions that are defined by the user to do a specific task. (soon)
# each built-in function has attributes that modifies its behavior like (end) int print() function.
# that modifies the default (\n) that goes to the next line, with any other character

print("Hello, World!")  # prints the string "Hello, World!" and goes to next line.
print("Let's Go!")  # pritns the string "Let's Go!" and goes to next line.

print(10, 12, 13)  # prints them on the same line but with spaces between them.

print()  # print nothing then goes to the next line, which is equivalent to print(end=\n)

print(10, end=" ")  # puts spaces instead of going to the next line
print(20, end="")  # cancels going to the next line
print(30)

string1 = "Hello, "
string2 = "World!"
print(string1 + string2)  # concatenates the two strings together.

age = 19

print(f"mohamed is {age} years old")  # first method for using (int) inside of a string.
print(
    f"Salah is {25} years old, while Alaa is {20} years old."
)  # first method for using (int) inside of a string.
print(
    "Kareem is {} years old, while Alaa is {} years old.".format(19, 20)
)  # second method by using empty {} and then using .format() to add them respectively.
print(
    "Ahmed is {0} years old, Alaa is {1}, Zaghloul is {other} and Fawzy is {other}".format(
        19, 20, other=30
    )  # you can add all same value to multiple places by using the name of the value.
    # ex: .format(other=30) and then using {other} in the string and it will be replaced by 30.
)
data = dict(
    age1="10", age2="20", other="30"
)  # defining the names age1, etc... in a dict, then using them down with .format(**"dict name")
print("Ahmed is {age1} years old, Alaa is {age2}, and Essam is {other}".format(**data))

print("apple price: %d EGP" % 50.3)  # %d stands for integer (cancels decimal points)
print("apple price: %.2f EGP, banana price: %.5f EGP" % (50.3, 32.003423))
# %f stands for float (decimal points) and .2 or any other number is the number of decimal points.

print("=" * 53)  # prints the character "=" 53 times. (you can use any other character)
