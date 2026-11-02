import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
df = pd.read_csv("books_eda_dataset.csv")

print("Dataset loaded successfully!")
print(df.head())
# Price Distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=8)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.show()
# Price Distribution
plt.figure(figsize=(8, 5))

plt.hist(df["Price"], bins=8)

plt.title("Distribution of Book Prices")
plt.xlabel("Price (£)")
plt.ylabel("Number of Books")

plt.show()
# Rating Distribution
plt.figure(figsize=(8, 5))

sns.countplot(x="Rating", data=df)

plt.title("Distribution of Book Ratings")
plt.xlabel("Rating")
plt.ylabel("Number of Books")

plt.show()
# Price vs Rating
plt.figure(figsize=(8, 5))

sns.scatterplot(x="Rating_Number", y="Price", data=df)

plt.title("Price vs Rating")
plt.xlabel("Rating")
plt.ylabel("Price (£)")

plt.show()
# Correlation Heatmap
plt.figure(figsize=(7, 5))

correlation = df[["Price", "Rating_Number"]].corr()

sns.heatmap(correlation, annot=True, cmap="coolwarm")

plt.title("Correlation between Price and Rating")
plt.show()
# Final EDA Findings

print("\n===== EDA FINDINGS =====")

print("Average Price:", round(df["Price"].mean(), 2))
print("Highest Price:", df["Price"].max())
print("Lowest Price:", df["Price"].min())

print("\nAverage Rating:", round(df["Rating_Number"].mean(), 2))

print("\nRating Counts:")
print(df["Rating"].value_counts())

print("\nCorrelation between Price and Rating:")
print(round(df["Price"].corr(df["Rating_Number"]), 2))