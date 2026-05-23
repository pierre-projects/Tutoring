"""
General Web Scraper Starter File

Goal:
Build a scraper that collects useful data from a webpage.

This file is incomplete on purpose.
The comments show examples, but the student still needs to inspect the site
and fill in the real tags/classes.

General scraper steps:
1. Choose a website
2. Inspect the HTML
3. Find the repeated item/card/container
4. Extract useful data from each item
5. Clean the data
6. Filter or sort the data
7. Save the results
"""

# -----------------------------
# Imports
# -----------------------------

# requests lets Python load a webpage.
# It works like a browser asking a website for HTML.
# Example:
# response = requests.get("https://example.com")
import requests

# BeautifulSoup helps us search through HTML.
# It lets us find tags, classes, links, text, and repeated cards.
# Example:
# soup = BeautifulSoup(response.text, "html.parser")
from bs4 import BeautifulSoup

# csv lets us save scraped data into a spreadsheet-style file.
# CSV files can open in Excel or Google Sheets.
# Example:
# writer = csv.DictWriter(file, fieldnames=["title", "price", "link"])
import csv

# urljoin helps us turn relative links into full links.
# Example:
# "product.html" becomes "https://example.com/product.html"
from urllib.parse import urljoin

# time lets us pause between requests.
# This is useful when scraping multiple pages.
# Example:
# time.sleep(1)
import time


# -----------------------------
# Settings / Constants
# -----------------------------

# TODO: Replace this with the website you want to scrape.
# Example:
# URL = "https://example.com/products"
URL = "PASTE_WEBSITE_URL_HERE"

# TODO: Use this if the website has relative links.
# Example:
# BASE_URL = "https://example.com"
BASE_URL = "PASTE_BASE_WEBSITE_URL_HERE"

# TODO: Name the file where results will be saved.
# Example:
# OUTPUT_FILE = "products.csv"
OUTPUT_FILE = "scraped_results.csv"

# TODO: Optional filter value.
# Example:
# MAX_PRICE = 30.00
# KEYWORD = "python"
# MIN_RATING = 4
FILTER_VALUE = "CHANGE_THIS"


# -----------------------------
# Step 1: Load the webpage
# -----------------------------

def get_page_html(url):
    """
    Concept:
    A scraper first needs to request the webpage.

    This function should:
    - send a GET request
    - check if the page loaded correctly
    - return the HTML text
    """

    # TODO: Send a request to the website.
    # Example:
    # response = requests.get(url)

    # TODO: Add a User-Agent if needed.
    # Example:
    # headers = {"User-Agent": "Mozilla/5.0"}
    # response = requests.get(url, headers=headers)

    # TODO: Check if the page loaded.
    # Example:
    # if response.status_code == 200:
    #     return response.text

    # TODO: Print an error if the page failed.
    # Example:
    # print("Page failed:", response.status_code)
    # return None

    pass


# -----------------------------
# Step 2: Find repeated items
# -----------------------------

def find_items(html):
    """
    Concept:
    Most scraper projects collect repeated items.

    Examples:
    - product cards
    - job listings
    - movie cards
    - news articles
    - event cards
    - search results

    This function should:
    - turn the HTML into a BeautifulSoup object
    - find all repeated item containers
    - return the list of item containers
    """

    # TODO: Create a BeautifulSoup object.
    # Example:
    # soup = BeautifulSoup(html, "html.parser")

    # TODO: Inspect the page and find the repeated container.
    # Example HTML:
    # <div class="item-card">...</div>
    #
    # Example code:
    # items = soup.find_all("div", class_="item-card")

    # Other possible examples:
    # items = soup.find_all("article")
    # items = soup.find_all("li", class_="result")
    # items = soup.select(".item-card")

    # TODO: Return the list of repeated items.
    # Example:
    # return items

    pass


# -----------------------------
# Step 3: Clean text
# -----------------------------

def clean_text(text):
    """
    Concept:
    Scraped text is often messy.

    It may include:
    - extra spaces
    - new lines
    - tabs
    - labels you do not need
    """

    # TODO: Check if the text is missing.
    # Example:
    # if text is None:
    #     return ""

    # TODO: Remove extra spaces and new lines.
    # Example:
    # cleaned = text.strip()

    # TODO: Replace line breaks with spaces.
    # Example:
    # cleaned = cleaned.replace("\n", " ")

    # TODO: Remove repeated spaces.
    # Example:
    # cleaned = " ".join(cleaned.split())

    # TODO: Return the cleaned text.
    # Example:
    # return cleaned

    pass


# -----------------------------
# Step 4: Clean numbers
# -----------------------------

def clean_number(number_text):
    """
    Concept:
    Websites store numbers as text.

    Examples:
    "$19.99" should become 19.99
    "1,200 views" should become 1200
    "Rating: 4.5" should become 4.5
    """

    # TODO: Clean the text first.
    # Example:
    # number_text = clean_text(number_text)

    # TODO: Remove symbols or labels.
    # Example:
    # number_text = number_text.replace("$", "")
    # number_text = number_text.replace(",", "")
    # number_text = number_text.replace("views", "")
    # number_text = number_text.replace("Rating:", "")

    # TODO: Convert the text to a number.
    # Example for decimals:
    # return float(number_text)

    # Example for whole numbers:
    # return int(number_text)

    pass


# -----------------------------
# Step 5: Parse one item
# -----------------------------

def parse_item(item):
    """
    Concept:
    This function extracts useful data from one item.

    One item could be:
    - one product
    - one job listing
    - one event
    - one article
    - one movie
    - one search result

    You should inspect the HTML first, then decide what data to collect.
    """

    # TODO: Extract a title or name.
    # Example HTML:
    # <h2 class="title">Cool Item</h2>
    #
    # Example code:
    # title_tag = item.find("h2", class_="title")
    # title = clean_text(title_tag.text)

    # TODO: Extract a detail like price, date, rating, location, or category.
    # Example HTML:
    # <p class="price">$19.99</p>
    #
    # Example code:
    # price_tag = item.find("p", class_="price")
    # price = clean_number(price_tag.text)

    # TODO: Extract a link.
    # Example HTML:
    # <a href="/details/item-1">View</a>
    #
    # Example code:
    # link_tag = item.find("a")
    # relative_link = link_tag["href"]
    # full_link = urljoin(BASE_URL, relative_link)

    # TODO: Return the data as a dictionary.
    # Example:
    # return {
    #     "title": title,
    #     "price": price,
    #     "link": full_link
    # }

    pass


# -----------------------------
# Step 6: Parse all items
# -----------------------------

def parse_all_items(items):
    """
    Concept:
    A scraper should collect multiple items, not just one.

    This function should:
    - loop through all item containers
    - parse each item
    - store each result in a list
    - return the full list
    """

    results = []

    # TODO: Loop through each item.
    # Example:
    # for item in items:

        # TODO: Parse one item.
        # Example:
        # parsed_item = parse_item(item)

        # TODO: Add the parsed item to the results list.
        # Example:
        # results.append(parsed_item)

    # TODO: Return all scraped results.
    return results


# -----------------------------
# Step 7: Filter results
# -----------------------------

def filter_results(results):
    """
    Concept:
    Filtering helps the scraper answer a useful question.

    Examples:
    - only items under $30
    - only jobs mentioning Python
    - only events this week
    - only products in stock
    - only movies above a certain rating
    """

    filtered = []

    # TODO: Loop through each result.
    # Example:
    # for result in results:

        # TODO: Write a rule.
        # Example for price:
        # if result["price"] <= 30:
        #     filtered.append(result)

        # Example for keyword:
        # if "python" in result["title"].lower():
        #     filtered.append(result)

        # Example for rating:
        # if result["rating"] >= 4:
        #     filtered.append(result)

    return filtered


# -----------------------------
# Step 8: Sort results
# -----------------------------

def sort_results(results):
    """
    Concept:
    Sorting makes the data easier to use.

    Examples:
    - cheapest to most expensive
    - newest to oldest
    - highest rating first
    - alphabetical order
    """

    # TODO: Choose what field to sort by.

    # Example: sort by price from lowest to highest.
    # return sorted(results, key=lambda item: item["price"])

    # Example: sort by rating from highest to lowest.
    # return sorted(results, key=lambda item: item["rating"], reverse=True)

    # Example: sort alphabetically by title.
    # return sorted(results, key=lambda item: item["title"])

    # If you do not want to sort yet, return the original list.
    return results


# -----------------------------
# Step 9: Save results
# -----------------------------

def save_to_csv(results, filename):
    """
    Concept:
    A scraper is more useful when the data is saved.

    CSV files can be opened in:
    - Excel
    - Google Sheets
    - Numbers
    """

    # TODO: Stop if there are no results.
    # Example:
    # if len(results) == 0:
    #     print("No results to save.")
    #     return

    # TODO: Get the column names from the dictionary keys.
    # Example:
    # fieldnames = results[0].keys()

    # TODO: Open the file.
    # Example:
    # with open(filename, "w", newline="", encoding="utf-8") as file:

        # TODO: Create the CSV writer.
        # Example:
        # writer = csv.DictWriter(file, fieldnames=fieldnames)

        # TODO: Write the header row.
        # Example:
        # writer.writeheader()

        # TODO: Write all result rows.
        # Example:
        # writer.writerows(results)

    pass


# -----------------------------
# Step 10: Display results
# -----------------------------

def print_results(results):
    """
    Concept:
    Good output should be easy to read.

    This helps you quickly check if the scraper worked.
    """

    # TODO: Loop through the results.
    # Example:
    # for result in results:

        # TODO: Print each result clearly.
        # Example:
        # print("-" * 40)
        # print("Title:", result["title"])
        # print("Price:", result["price"])
        # print("Link:", result["link"])

    pass


# -----------------------------
# Optional Step 11: Scrape multiple pages
# -----------------------------

def scrape_multiple_pages():
    """
    Concept:
    Some websites have more than one page of results.

    Only do this after one page works.
    """

    all_results = []

    # TODO: Loop through page numbers.
    # Example:
    # for page_number in range(1, 4):

        # TODO: Build a page URL.
        # Example:
        # page_url = f"https://example.com/page/{page_number}"

        # TODO: Load that page.
        # Example:
        # html = get_page_html(page_url)

        # TODO: Find and parse the items.
        # Example:
        # items = find_items(html)
        # results = parse_all_items(items)

        # TODO: Add results to the full list.
        # Example:
        # all_results.extend(results)

        # TODO: Pause between requests.
        # Example:
        # time.sleep(1)

    return all_results


# -----------------------------
# Main program
# -----------------------------

def main():
    """
    Main scraper flow:

    1. Load the webpage
    2. Find repeated items
    3. Parse each item
    4. Filter the results
    5. Sort the results
    6. Print the results
    7. Save the results
    """

    # TODO: Load the webpage.
    # Example:
    # html = get_page_html(URL)

    # TODO: Stop if the page failed.
    # Example:
    # if html is None:
    #     print("Could not load page.")
    #     return

    # TODO: Find the repeated item containers.
    # Example:
    # items = find_items(html)

    # TODO: Parse all items.
    # Example:
    # results = parse_all_items(items)

    # TODO: Print how many items were scraped.
    # Example:
    # print("Items scraped:", len(results))

    # TODO: Filter results.
    # Example:
    # filtered_results = filter_results(results)

    # TODO: Sort results.
    # Example:
    # sorted_results = sort_results(filtered_results)

    # TODO: Print results.
    # Example:
    # print_results(sorted_results)

    # TODO: Save results.
    # Example:
    # save_to_csv(sorted_results, OUTPUT_FILE)

    pass


# This runs the program only when this file is executed directly.
# It will not run automatically if this file is imported into another file.
if __name__ == "__main__":
    main()