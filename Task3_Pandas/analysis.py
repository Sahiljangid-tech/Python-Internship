import pandas as pd

# Load CSV file
df = pd.read_csv("sales_data.csv")

print("Original Data:")
print(df)

# Cleaning
df = df.dropna()

print("\nSummary Statistics:")
print(df.describe())

# Filter data
electronics = df[df["Category"] == "Electronics"]

print("\nElectronics Products:")
print(electronics)

# Grouping
grouped = df.groupby("Category")["Sales"].sum()

print("\nTotal Sales by Category:")
print(grouped)

# Insights
highest_sale = df.loc[df["Sales"].idxmax()]

print("\nHighest Selling Product:")
print(highest_sale)