import pandas as pd

df = pd.read_csv("data.csv")

print("\nFirst 5 rows:\n", df.head())

print("\nDataset Info:")
print(df.info())

print("\nBasic Statistics:\n", df.describe())