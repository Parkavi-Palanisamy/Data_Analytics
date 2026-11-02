import requests
from bs4 import BeautifulSoup
import pandas as pd

# Website URL
url = "https://books.toscrape.com/"

# Get website data
response = requests.get(url)

print("Status Code:", response.status_code)

# Parse HTML
soup = BeautifulSoup(response.text, "html.parser")

# Find all books
books = soup.find_all("article", class_="product_pod")

print("Number of books:", len(books))

# Lists to store data
book_names = []
prices = []
ratings = []

# Extract book information
for book in books:

    # Book name
    name = book.h3.a["title"]
    book_names.append(name)

    # Price
    price = book.find("p", class_="price_color").text
    prices.append(price)

    # Rating
    rating = book.find("p", class_="star-rating")["class"][1]
    ratings.append(rating)

# Create dataset
data = {
    "Book Name": book_names,
    "Price": prices,
    "Rating": ratings
}

df = pd.DataFrame(data)

# Display final dataset
print("\nFinal Dataset:")
print(df)

# Save dataset as CSV
df.to_csv("books_dataset.csv", index=False)

print("\nDataset saved successfully!")