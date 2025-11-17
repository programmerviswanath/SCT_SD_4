"""
   TASK-4 : Create a program that extracts product information, such as names, prices, and 
   ratings, from an online e-commerce website and stores the data in a structured format like a CSV file.
"""
import requests
from bs4 import BeautifulSoup
import csv

# URL of website
url = "https://books.toscrape.com/"

# Send request
page = requests.get(url)
soup = BeautifulSoup(page.text, "html.parser")

# Find all products
products = soup.find_all("article", class_="product_pod")

# List to store scraped data
data = []

for p in products: 
    # Product name
    name = p.h3.a["title"]
    # Price
    price = p.find("p", class_="price_color").text
    # Rating (converted from text class)
    rating_class = p.find("p")["class"][1]
    data.append([name, price, rating_class])

# Save to CSV
with open("products.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["Name", "Price", "Rating"])
    writer.writerows(data)

print("Scraping Completed! Saved as products.csv")
