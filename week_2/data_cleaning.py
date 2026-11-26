
import pandas as pd

df = pd.read_csv("students.csv")

print("Original Dataset:")
print(df.head())

print("\nOriginal Dataset Shape:")
print(df.shape)


df.columns = df.columns.str.strip()

df["gender"] = df["gender"].astype("string").str.strip().str.lower()
df["city"] = df["city"].astype("string").str.strip()
df["name"] = df["name"].astype("string").str.strip()


df["gender"] = df["gender"].replace({
    "m": "male",
    "f": "female"
})


df["attendance_pct"] = (
    df["attendance_pct"]
    .astype("string")
    .str.replace("%", "")
)

df["attendance_pct"] = pd.to_numeric(
    df["attendance_pct"], errors="coerce"
)

numeric_columns = [
    "age",
    "study_hours",
    "sleep_hours",
    "score"
]

for col in numeric_columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")


df.loc[~df["age"].between(10, 25), "age"] = pd.NA

df.loc[
    ~df["study_hours"].between(0, 24),
    "study_hours"
] = pd.NA

df.loc[
    ~df["sleep_hours"].between(0, 24),
    "sleep_hours"
] = pd.NA

df.loc[
    ~df["attendance_pct"].between(0, 100),
    "attendance_pct"
] = pd.NA

df.loc[
    ~df["score"].between(0, 100),
    "score"
] = pd.NA


print("\nMissing Values Before Filling:")
print(df.isnull().sum())


for col in numeric_columns + ["attendance_pct"]:
    df[col] = df[col].fillna(df[col].median())



df = df.drop_duplicates()


print("\nCleaned Dataset:")
print(df.head())

print("\nCleaned Dataset Information:")
df.info()

print("\nMissing Values After Cleaning:")
print(df.isnull().sum())

print("\nFinal Dataset Shape:")
print(df.shape)

df.to_csv("cleaned_students.csv", index=False)

print("\nCleaned dataset saved successfully!")
