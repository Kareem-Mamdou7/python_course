import pandas as pd

groceries = pd.Series(
    data=[30, 6, "Yes", "No"], index=["eggs", "apples", "milk", "bread"]
)

print(groceries)
print(groceries.shape)
print(groceries.ndim)
print(groceries.size)

print()
print()

print(groceries.values)
print(groceries.index)

print()
print("bananas" in groceries)
print("bread" in groceries)

print()
print(groceries["eggs"])

print()
print(groceries[["milk", "bread"]])

print()
print(groceries[[0, 1]])

print()
print()
print(groceries.iloc[[2, 3]])
print()
print(groceries.loc[["bread", "milk"]])

print()
print(groceries)
groceries["eggs"] = 12
print()
print(groceries)

groceries = groceries.drop(
    "apples"
)  # groceries.drop("apples", inplace = True) are the same
print()
print(groceries)

fruits = pd.Series(data=[10, 6, 3], index=["apples", "oranges", "bananas"])
print()
print(fruits)

fruits *= 2  # you can perform operations on each data one by one
print()
print(fruits)
