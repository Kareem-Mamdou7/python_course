import numpy as np

x = np.array([1, 2, 3, 4, 5])
print("x=", x)

print(type(x))

print("the elements in x are of type:", x.dtype)

print("x has dimensions of:", x.shape)

y = np.array(["Hello", "World"])
print(y)
print(y.dtype)

x = np.array([1, "Hello"])
print(x)
print(x.dtype)

x = np.array([1, 2, 3])
y = np.array([1.5, 2.5, 3.5])
z = np.array([1.5, 2, 3])

print(x.dtype, y.dtype, z.dtype)

x = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12]])

print(x)
print(x.shape)
print(x.size, x.dtype)
print(type(x))

np.save("my_array", x)

k = np.load("my_array.npy")

print(k)
print()
print()
x = np.zeros((3, 4))
print(x)
x = np.ones((3, 4))
print(x)

print()
x = np.full((3, 4), 5)
print(x)

print()
x = np.eye(3)
print(x)

print()
x = np.diag([10, 20, 30, 40])
print(x)

print()
x = np.arange(1, 14, 3)
print(x)

print()
x = np.linspace(1, 10)
print(x)

print()
x = np.arange(20)
print(x)

print()
x = np.reshape(x, (4, 5))
print(x)

print()
x = np.arange(20).reshape(5, 4)
print(x)

x = np.random.randint(4, 15, size=(3, 2))
print(x)

print(x[2][0])

x = np.array([1, 2, 3, 4, 5])
print(x)

y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(y)

x = np.delete(x, [0, -1])
print(x)

y = np.delete(y, 0, axis=0)
print(y)

x = np.array([1, 2, 3, 4, 5])
x = np.append(x, [6, 7])
print(x)

y = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
y = np.append(y, [[10], [10], [10]], axis=1)
y = np.append(y, [[11, 11, 11, 11]], axis=0)

print(y)

z = np.copy(y[1:4, 2:5])
print()
print()
print(z)

print()
print(np.exp(z))  # e^z

print()
print(np.sqrt(z))

print()
print(np.power(z, 2))
