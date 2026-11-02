import pandas as pd
import numpy as np

# STEP 1: Load the dataset
df = pd.read_csv("books_dataset.csv")

print("Dataset loaded successfully!")

# STEP 2: Display first 5 rows
print("\nFirst 5 Rows:")
print(df.head())

# STEP 3: Check number of rows and columns
print("\nDataset Shape:")
print(df.shape)

# STEP 4: Display column names
print("\nColumn Names:")
print(df.columns.tolist())

# STEP 5: Check data types
print("\nData Types:")
print(df.dtypes)

# STEP 6: Check missing values
print("\nMissing Values:")
print(df.isnull().sum())

# STEP 7: Check duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# STEP 8: Convert Price to numeric format
df["Price"] = df["Price"].str.extract(r'(\d+\.\d+)')[0].astype(float)

print("\nUpdated Price:")
print(df["Price"].head())
# Price statistics
print("\nPrice Statistics:")
print(df["Price"].describe())
# Convert Rating into numbers
rating_map = {
    "One": 1,
    "Two": 2,
    "Three": 3,
    "Four": 4,
    "Five": 5
}

df["Rating_Number"] = df["Rating"].map(rating_map)

print("\nRating Numbers:")
print(df[["Rating", "Rating_Number"]].head())
# Calculate average rating
print("\nAverage Rating:")
print(df["Rating_Number"].mean())
# Rating distribution
print("\nRating Distribution:")
print(df["Rating"].value_counts())
# Find the highest priced book
print("\nHighest Priced Book:")
print(df.loc[df["Price"].idxmax()])
# Find the lowest priced book
print("\nLowest Priced Book:")
print(df.loc[df["Price"].idxmin()])
# Save the analyzed dataset
df.to_csv("books_eda_dataset.csv", index=False)

print("\nEDA dataset saved successfully!")