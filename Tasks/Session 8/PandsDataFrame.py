import pandas as pd

items = {
    "Bob": pd.Series(data=[245, 25, 55], index=["bike", "pants", "watch"]),
    "Alice": pd.Series(
        data=[40, 110, 500, 45], index=["book", "glasses", "bike", "pants"]
    ),
}

print(type(items))

print()
shopping_carts = pd.DataFrame(items)
print(shopping_carts)

print()
print(shopping_carts.shape)

print()
print(shopping_carts.ndim)

print()
print(shopping_carts.size)

print()
print(shopping_carts.values)

print()
print(shopping_carts.index)

print()
print(shopping_carts.columns)

part_shopping_carts = pd.DataFrame(items, index=["pants", "bike"])
print()
print(part_shopping_carts)

alice_shopping_cart = pd.DataFrame(items, index=["pants", "bike"], columns=["Alice"])
print()
print(alice_shopping_cart)

data = {
    "Bob": [245, 25, 55],
    "Alice": [40, 110, 500],
}

df = pd.DataFrame(data)
print()
print(df)

df = pd.DataFrame(data, index=["l1", "l2", "l3"])
print()
print(df)

print(df[["Bob"]].iloc[2])
