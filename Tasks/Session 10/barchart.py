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
plt.figure(figsize=(10, 5))

df.groupby("Department")["Min_Salary"].mean().sort_values().plot(
    kind="bar", color="blue"
)

plt.xlabel("Department", fontsize=12)
plt.ylabel("Avg Min Salary ($)", fontsize=12)
plt.title("Average Salary by Department", fontsize=14)

plt.grid(axis="y", linestyle="-", alpha=0.5)

plt.xticks(rotation=45)

plt.show()
