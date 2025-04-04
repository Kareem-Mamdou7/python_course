import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("la_jobs.csv")
print(data)

print("#" * 100)
print()

# Data Cleaning
data.drop(
    str(data.columns[0]),
    axis=1,
    inplace=True,  # delete the first index in my dataset so it's not duplicated
)  # data = pd.read_csv("la_jobs.csv", index_col=0) to set my first column as index and don't create a default index one
print(data)

print()
print()
print(data.shape)
print(data.info())

data.replace("-", np.nan, inplace=True)  # replaces the "-" with null using numpy
print(data.isna().sum())  # number of null in each file
print(data.isna())  # True if null, False if not null

data.replace(
    np.nan, "Missing", inplace=True
)  # data.fillna("Missing", inplace=True) is the same thing
print(data)

data.replace("Missing", np.nan, inplace=True)
print(data.dropna())
