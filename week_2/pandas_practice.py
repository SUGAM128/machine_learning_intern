
import pandas as pd


df = pd.read_csv("students.csv")
print("First Five Rows:")
print(df.head())

print("\nDataset Information:")
df.info()
print("\nStatistical Summary:")
print(df.describe())

print("\nDataset Shape:")
print(df.shape)

# data filterig

print("\nStudents with score greater than 80:")
filtered_data = df[df["score"] > 80]
print(filtered_data[["name", "city", "score"]])


# data sorting

print("\nStudents sorted by score (highest first):")
sorted_data = df.sort_values(by="score", ascending=False)
print(sorted_data[["name", "score"]])


# grouped data

print("\nAverage score by city:")
grouped_data = df.groupby("city")["score"].mean()
print(grouped_data)


# missing va;ues

print("\nMissing Values:")
print(df.isnull().sum())

df["score"] = df["score"].fillna(df["score"].mean())
df["sleep_hours"] = df["sleep_hours"].fillna(df["sleep_hours"].mean())


# duplication

print("\nDuplicate Records:")
print(df[df.duplicated()])

df = df.drop_duplicates()

print("\nDataset after removing duplicates:")
print(df.shape)


# data merging

city_summary = df.groupby("city")["score"].mean().reset_index()
merged_data = pd.merge(df, city_summary, on="city", suffixes=("", "_city_avg"))

print("\nMerged Dataset:")
print(merged_data[["name", "city", "score", "score_city_avg"]])

