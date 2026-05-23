"""
General Web Scraper Starter File

Goal:
Build a scraper that collects useful data from a webpage.

This file is incomplete on purpose.
You will fill in each section as you learn the concepts.

General scraper steps:
1. Choose a website
2. Inspect the HTML
3. Find the repeating item/card/container
4. Extract useful data from each item
5. Clean the data
6. Filter or sort the data
7. Save the results
"""

# -----------------------------
# Imports
# -----------------------------

# TODO: import requests
# TODO: import BeautifulSoup from bs4
# TODO: import csv
# TODO: import urljoin from urllib.parse if the site has links


# -----------------------------
# Settings / Constants
# -----------------------------

# TODO: Replace this with the website you want to scrape
URL = "PASTE_WEBSITE_URL_HERE"

# TODO: Use this if the website has relative links
BASE_URL = "PASTE_BASE_WEBSITE_URL_HERE"

# TODO: Name the file where results will be saved
OUTPUT_FILE = "scraped_results.csv"


# -----------------------------
# Step 1: Load the webpage
# -----------------------------

def get_page_html(url):
    """
    Concept:
    A scraper first needs to request the webpage.

    This function should:
    - send a request to the URL
    - check if the page loaded correctly
    - return the HTML text
    """

    # TODO: send a GET request using requests.get()

    # TODO: check the status code

    # TODO: return the HTML if the status code is 200

    # TODO: return None if the page failed

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

    # TODO: create a BeautifulSoup object

    # TODO: inspect the website and find the repeated container

    # Example:
    # items = soup.find_all("div", class_="item-card")

    # TODO: return the list of items

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

    This function should clean text before saving it.
    """

    # TODO: remove extra spaces

    # TODO: remove new lines

    # TODO: return the cleaned text

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

    This function should convert scraped number text into a usable number.
    """

    # TODO: remove symbols like $, commas, or labels

    # TODO: convert the result to int or float

    # TODO: return the number

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

    # TODO: extract the title/name

    # TODO: extract a price/date/rating/category/etc.

    # TODO: extract a link if the item has one

    # TODO: clean the extracted data

    # TODO: return the data as a dictionary

    # Example return:
    # return {
    #     "title": title,
    #     "detail": detail,
    #     "link": link
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

    # TODO: loop through each item

    # TODO: call parse_item(item)

    # TODO: append the parsed data to results

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

    # TODO: loop through results

    # TODO: check if each result matches your rule

    # TODO: append matching results to filtered

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

    # TODO: choose what field to sort by

    # Example:
    # return sorted(results, key=lambda item: item["price"])

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

    if len(results) == 0:
        print("No results to save.")
        return

    # TODO: get the fieldnames from the dictionary keys

    # TODO: open the CSV file

    # TODO: create a DictWriter

    # TODO: write the header

    # TODO: write all rows

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

    # TODO: loop through results

    # TODO: print each result clearly

    pass


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

    # TODO: get the HTML

    # TODO: stop if the HTML did not load

    # TODO: find repeated items

    # TODO: parse all items

    # TODO: filter results

    # TODO: sort results

    # TODO: print results

    # TODO: save results to CSV

    pass


if __name__ == "__main__":
    main()