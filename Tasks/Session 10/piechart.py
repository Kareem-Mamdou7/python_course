import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

departments = ["IT", "HR", "Finance", "Sales", "Marketing", "Engineering"]
genders = ["Male", "Female"]

data = {
    "Employee_ID": np.arange(101, 151),
    "Department": np.random.choice(departments, 50),
    "Experience": np.random.randint(1, 30, 50),
    "Min_Salary": np.random.randint(40000, 120000, 50),
    "Max_Salary": np.random.randint(60000, 180000, 50),
    "Performance_Rating": np.random.randint(1, 5, 50),
    "Gender": np.random.choice(genders, 50),
}

df = pd.DataFrame(data)
plt.figure(figsize=(6, 6))

df["Gender"].value_counts().plot.pie(
    autopct="%1.1f%%", colors=["lightblue", "pink"], startangle=140
)

plt.title("Gender Distribution", fontsize=14)
plt.ylabel("Gender")
plt.show()
