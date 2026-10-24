import numpy as np
import pandas as pd
df=pd.read_csv("data/StudentsPerformance.csv")
print(df)

# check missing data
print("missing values")
print(df.isnull().sum())
# handle missing data
numeric_cols = df.select_dtypes(include=np.number).columns

df[numeric_cols] = df[numeric_cols].fillna(
    df[numeric_cols].mean()
)
#remove duplicacy
df=df.drop_duplicates()
#calculate total and average marks
subject_cols = [
    col for col in ["Math", "Science", "English"]
    if col in df.columns
]

if subject_cols:
    df["Total_Marks"] = df[subject_cols].sum(axis=1)
    df["Average_Marks"] = df[subject_cols].mean(axis=1)
#describe stat summary
print(df.describe())
# highest scores
if "Average_Marks" in df.columns and not  df.empty:
    top_student=df.loc[df["Average_Marks"].indxmax()]
    print("\n highest scoring student:")
    print(top_student)
# SORT STUDENTS BY AVERAGE MARKS
if "Average_Marks" in df.columns:
    df=df.sort_values(by="Average_Marks", decending=False)
# Save the cleaned dataset
df.to_csv("cleaned_data", index=False)
print("\n data analysis completed")