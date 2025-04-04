import pandas as pd

df = pd.read_csv("goog-1.csv")
print(df)

print(df.head())
print(df.tail())

print()
print(df.shape)

print()
print(df.info())

print()
print(df.describe())

print()
print(df["Open"].mean())

print()
print(df.columns)

print()
print(df[df["Open"] > 300])

print()
print(df.isnull().sum())
