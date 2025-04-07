import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

data = pd.read_csv("tmdb_5000_movies.csv")
df = pd.DataFrame(data)
print(df.head(10))
