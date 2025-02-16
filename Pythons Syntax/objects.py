a = 10
b = 20
print(id(a), id(b))  # prints the address of a and b in memory

b = a
print(id(a), id(b))  # b now has the same address as a

b = 42
print(a)  # a changes as b changes (they're the same thing with different names)
print()

print(a)

a = a + 20
print(a)

a += 30
print(a)

x = y = z = 2  # assign 2 to x, y, and z and have the same address in memory

a, b, c = 1, 5, 9  # assign 1 to a, 5 to b, and 9 to c

i = 1  # integer (no floating point)
f = 1.8  # flaot (floating point)
c = 1 + 3j  # complex number
s = "apple"  # string, or 'apple'
l = [1, "hi"]  # list
t = ("thing", "to do")  #

x = 12e2  # the same as 12 * 10^2
print(x)

# how to change type:
a = 5
print(float(a))  # 5.0

print()

a = 2.8
print(int(a))  # 2

print()

a = 3
print(complex(a))  # 3 + 0j

b = 50
print(isinstance(b, int))  # True becaue a is an integer
print(isinstance(b, float))  # False because a is not a float

x = "a"
print(x * 3)  # aaa types (a) 3 times
print("aaa" == 3 * "a")  # True as they give the same output
print(f"x = {x}")  # prints the value of x
