import random

# print random integer or float (changes for each run)
print(random.randint(1, 100))
print(random.random())

# Generate random number within a range

print(random.randrange(3, 9))

# get the exact random number each run
random.seed(0)
print(random.random())
