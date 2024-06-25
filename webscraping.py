import requests
from bs4 import BeautifulSoup
import json
import os

# Define the URL of the website to scrape
url = "https://www.amazon.com/s?k=smartphones&_encoding=UTF8&content-id=amzn1.sym.061f5f08-3bb1-4c70-8051-5d850a92de53&pd_rd_r=5a1be806-de8b-42d3-accb-2966b7965e37&pd_rd_w=XMc6L&pd_rd_wg=ZwkJ4&pf_rd_p=061f5f08-3bb1-4c70-8051-5d850a92de53&pf_rd_r=HER51Z8KQ5NP0SQDJ9V0&ref=pd_hp_d_atf_unk"

try:
    # Send a request to fetch the HTML content of the page
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for bad status codes
except requests.RequestException as e:
    print("Failed to retrieve the webpage:", e)
    exit()

# Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the product details (name, price, rating)
# This part should be customized according to the structure of the webpage you are scraping
# You need to inspect the webpage to find the correct HTML elements to scrape
# Here's a hypothetical example:
products = soup.find_all("div", class_="product")

# Create a list to store the extracted data
product_data = []

for product in products:
    try:
        name = product.find("h2", class_="a-size-mini a-spacing-none a-color-base s-line-clamp-4").text.strip()
        price = product.find("span", class_="a-offscreen").text.strip()
        rating = product.find("span", class_="a-declarative").text.strip()
        product_data.append({"Name": name, "Price": price, "Rating": rating})
        print("Name:", name)
        print("Price:", price)
        print("Rating:", rating)
    except AttributeError as e:
        print("Failed to extract product data:", e)

# Define the JSON file path
current_directory = os.getcwd()
json_file = os.path.join(current_directory, "products.json")

# Write the extracted data to the JSON file
try:
    with open(json_file, mode="w", encoding="utf-8") as file:
        json.dump(product_data, file, indent=4)
    print(f"Data has been written to {json_file}")
except IOError as e:
    print("Failed to write data to JSON file:", e)
