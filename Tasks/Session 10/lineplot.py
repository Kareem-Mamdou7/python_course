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

sns.lineplot(
    x=df["Experience"], y=df["Min_Salary"], markers="o", linestyle="-", color="b"
)

plt.xlabel("Experience (Years)", fontsize=12)
plt.ylabel("Min_Salary ($)", fontsize=12)
plt.title("Salary Growth Over Experience", fontsize=14)

plt.grid(True, linestyle="-", alpha=0.5)
plt.show()
