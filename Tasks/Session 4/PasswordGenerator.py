import random

letters = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
    "A",
    "B",
    "C",
    "D",
    "E",
    "F",
    "G",
    "H",
    "I",
    "J",
    "K",
    "L",
    "M",
    "N",
    "O",
    "P",
    "Q",
    "R",
    "S",
    "T",
    "U",
    "V",
    "W",
    "X",
    "Y",
    "Z",
]
numbers = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
symbols = ["!", "#", "$", "%", "&", "(", ")", "*", "+"]

for i in range(4):
    print(random.choice(letters), end="")
for i in range(2):
    print(random.choice(symbols), end="")
for i in range(3):
    print(random.choice(numbers), end="")

print()
print()

myList = []
for i in range(4):
    myList.append(random.choice(letters))
for i in range(2):
    myList.append(random.choice(symbols))
for i in range(3):
    myList.append(random.choice(numbers))

for i in range(10):
    print(random.choice(myList), end="")
