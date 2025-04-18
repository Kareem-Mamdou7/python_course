import pandas as pd
import numpy as np

# Load the data
df = pd.read_csv("la_jobs.csv")

# Q1: Best job for a non-experienced job seeker
non_exp_jobs = df[df["EXPERIENCE_LENGTH"].isna() | (df["EXPERIENCE_LENGTH"] == 0)]
q1_answer = (
    non_exp_jobs[["JOB_CLASS_TITLE", "ENTRY_SALARY_GEN"]]
    .sort_values("ENTRY_SALARY_GEN", ascending=False)
    .head(5)
)
print("Q1: Top 5 jobs for non-experienced seekers:")
print(q1_answer.to_string(index=False))
print("\n")

# Q2: Best school type for future success
# Make sure SCHOOL_TYPE exists or adjust according to the dataset
if "SCHOOL_TYPE" in df.columns:
    school_types = df["SCHOOL_TYPE"].value_counts()
    print("Q2: Most required school types:")
    print(school_types)
    print("\nMost required school type is:", school_types.idxmax())
else:
    print("Q2: SCHOOL_TYPE column is not available in the dataset.")
print("\n")

# Q3: Best time of year to apply for jobs
df["OPEN_DATE"] = pd.to_datetime(df["OPEN_DATE"], errors="coerce")
# Ensure OPEN_DATE was parsed successfully before proceeding
if df["OPEN_DATE"].isnull().sum() == 0:
    monthly_openings = df["OPEN_DATE"].dt.month.value_counts().sort_index()
    month_names = [
        "Jan",
        "Feb",
        "Mar",
        "Apr",
        "May",
        "Jun",
        "Jul",
        "Aug",
        "Sep",
        "Oct",
        "Nov",
        "Dec",
    ]
    print("Q3: Job openings by month:")
    print(
        pd.DataFrame({"Month": month_names, "Openings": monthly_openings}).to_string(
            index=False
        )
    )
    best_months = monthly_openings.nlargest(3).index
    print("\nBest months to apply:", [month_names[m - 1] for m in best_months])
else:
    print("Q3: OPEN_DATE column contains missing or invalid values.")
print("\n")

# Q4: Experience vs Education importance
exp_vs_edu = df[["EXPERIENCE_LENGTH", "EDUCATION_YEARS"]].notna().sum()
print("Q4: Experience vs Education requirements:")
print(f"Number of jobs requiring experience: {exp_vs_edu['EXPERIENCE_LENGTH']}")
print(f"Number of jobs requiring education: {exp_vs_edu['EDUCATION_YEARS']}")
if exp_vs_edu["EXPERIENCE_LENGTH"] > exp_vs_edu["EDUCATION_YEARS"]:
    print("Conclusion: Experience is more important than education")
else:
    print("Conclusion: Education is more important than experience")
print("\n")

# Q5: Fresh grad jobs with future opportunities
# Ensure that 'EXP_JOB_CLASS_TITLE' exists or adjust this part
if "EXP_JOB_CLASS_TITLE" in df.columns:
    entry_level = df[df["EXPERIENCE_LENGTH"] <= 1]
    future_opportunities = entry_level[
        entry_level["JOB_CLASS_TITLE"].isin(df["EXP_JOB_CLASS_TITLE"])
    ]
    q5_answer = (
        future_opportunities[["JOB_CLASS_TITLE", "ENTRY_SALARY_GEN"]]
        .sort_values("ENTRY_SALARY_GEN", ascending=False)
        .head(5)
    )
    print("Q5: Top entry-level jobs with future opportunities:")
    print(q5_answer.to_string(index=False))
else:
    print("Q5: EXP_JOB_CLASS_TITLE column is not available in the dataset.")
