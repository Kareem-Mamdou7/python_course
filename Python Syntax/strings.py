# Strings are like arrays
a = "Hello, World!"
print(a[0])  # H as we start from 0
print(a[1])  # e
print(a[5])  # ,
print(a[6])  # W
print(a[-1])  # ! because the negative starts from the end (right)

b = "banana"
c = len(b)
print(c)  # prints the length of b (6)
print(len(b))  # you can print it directly without saving it in a variable

txt = "I Will be a great programmer"
print("great" in txt)  # prints (True) because "great" is in txt
print("programmer" not in txt)  # prints (False) because "programmer" is in txt
print("Hello" not in txt)  # prints (True) because "Hello" is not in txt

string = "Lets's learn Python"

# print line with 40 characters with (string) centered and other empty spaces filled with (#)
print(string.center(40, "#"))

# same with 30 characters and "*" instead of "#"
print(string.center(30, "*"))

# puts (string) on the left and filling the rest of the 40 characters with "#"
print(string.ljust(40, "#"))

# same but (string) on the right
print(string.rjust(40, "#"))

print(string.upper())  # prints the string in uppercase

string = "HELLO, WORLD!"
print(string.lower())  # prints the string in lowercase

string = "        Welcome to Python!        "
# removes any whitespace from the beginning or the end
print(string.strip())

# removes any whitespace from the beginning only
print(string.lstrip())

# removes any whitespace from the end only
print(string.rstrip())

# replace letters
a = "Jello, World!"
print(a.replace("J", "H"))

# split
print(
    a.split(",")
)  # splits the string into two strings at the character we chose (",")

# check if the strings are in uppercase or lowercase
c = "WEEEEE"
d = "weeeee"

print(c.isupper())  # prints (True) because all the letters are in uppercase
print(d.islower())  # prints (True) because all the letters are in lowercase
print(c.islower())  # prints (False) because all the letters are in uppercase

a = "i love python"
print(a.title())  # prints the first letter of each word in uppercase as in titles
