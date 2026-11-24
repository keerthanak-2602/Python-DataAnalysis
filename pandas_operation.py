
import pandas as pd

# 1. Load CSV and display basic information
df = pd.read_csv("C:/Users/keert/Downloads/sales.csv")

print("1. BASIC INFORMATION")
print(df.head())
print("\nDataset Information:")
df.info()
print("\nStatistical Summary:")
print(df.describe())

# 2. Handle missing values and duplicates
print("\n2. MISSING VALUES")
print(df.isnull().sum())

# Fill missing numerical values with mean
df.fillna(df.select_dtypes(include="number").mean(), inplace=True)

# Remove duplicate rows
df.drop_duplicates(inplace=True)

print("\nCleaned Dataset:")
print(df)
print("\nDuplicates:", df.duplicated().sum())

# 3. Group by category and find total revenue
print("\n3. TOTAL REVENUE BY CATEGORY")
result = df.groupby("Category")["Revenue"].sum()
print(result)

# 4. Sort by multiple columns
print("\n4. SORTED DATA")
sorted_df = df.sort_values(
    by=["Category", "Revenue"],
    ascending=[True, False]
)
print(sorted_df)

# 5. Create correlation matrix
print("\n5. CORRELATION MATRIX")
numeric_df = df.select_dtypes(include="number")
correlation = numeric_df.corr()
print(correlation)
