import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data = pd.read_csv("la_jobs.csv")
print(data)
print(data.columns)
data.replace("-", "0", inplace=True)
print(data["REQUIREMENT_SUBSET_ID"].unique().sum())
print(data["REQUIREMENT_SUBSET_ID"].value_counts())

print(data[data["REQUIREMENT_SUBSET_ID"] == "a"])
print(data.loc[3])

# changing the datatype of the columns

data["JOB_CLASS_NO"] = data["JOB_CLASS_NO"].astype(float, errors="raise")

data["OPEN_DATE"] = pd.to_datetime(
    data["OPEN_DATE"], format="%m-%d-%y", errors="coerce"
)

data["YEAR"] = data["OPEN_DATE"].dt.year
