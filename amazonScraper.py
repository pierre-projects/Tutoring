"""
Amazon Item Parser Starter File

Goal:
Parse one saved Amazon product page and extract useful item data.

Important:
This does NOT send requests to Amazon.
It reads a saved HTML file from your computer.

Why:
Amazon pages are complicated, dynamic, and not ideal for a first live scraper.
This version teaches the same scraping concepts safely.
"""

import csv
from bs4 import BeautifulSoup


HTML_FILE = "amazon_item.html"
OUTPUT_FILE = "amazon_item_data.csv"


# -----------------------------
# Step 1: Load local HTML file
# -----------------------------

def load_html_file(filename):
    """
    Concept:
    Instead of requesting a website, we open a saved HTML file.

    This lets us practice scraping without sending requests to Amazon.
    """

    # TODO: open the file using with open()

    # Example:
    # with open(filename, "r", encoding="utf-8") as file:
    #     return file.read()

    pass


# -----------------------------
# Step 2: Clean text
# -----------------------------

def clean_text(text):
    """
    Concept:
    Scraped text often has extra spaces and new lines.

    Example:
    '\\n    Product Name    \\n'

    Should become:
    'Product Name'
    """

    # TODO: handle missing text

    # TODO: strip spaces

    # TODO: replace repeated whitespace

    # Example:
    # return " ".join(text.split())

    pass


# -----------------------------
# Step 3: Extract title
# -----------------------------

def get_title(soup):
    """
    Concept:
    Amazon product titles are often stored in an element with id="productTitle".

    Example:
    <span id="productTitle">Some Product Name</span>
    """

    # TODO: find element with id="productTitle"

    # Example:
    # title_tag = soup.find(id="productTitle")

    # TODO: return cleaned title text

    pass


# -----------------------------
# Step 4: Extract price
# -----------------------------

def get_price(soup):
    """
    Concept:
    Prices are sometimes split across multiple tags.

    Amazon often stores readable prices inside class="a-offscreen".

    Example:
    <span class="a-offscreen">$29.99</span>
    """

    # TODO: find a price tag

    # Example:
    # price_tag = soup.find("span", class_="a-offscreen")

    # TODO: return cleaned price text

    pass


# -----------------------------
# Step 5: Extract rating
# -----------------------------

def get_rating(soup):
    """
    Concept:
    Ratings may be stored inside text like:

    '4.6 out of 5 stars'

    We can keep it as text first.
    Later, we could clean it into a number.
    """

    # TODO: find rating element

    # Possible example:
    # rating_tag = soup.find("span", class_="a-icon-alt")

    # TODO: return cleaned rating text

    pass


# -----------------------------
# Step 6: Extract review count
# -----------------------------

def get_review_count(soup):
    """
    Concept:
    Review count is often near id="acrCustomerReviewText".

    Example:
    '12,345 ratings'
    """

    # TODO: find element with id="acrCustomerReviewText"

    # TODO: return cleaned review count text

    pass


# -----------------------------
# Step 7: Extract availability
# -----------------------------

def get_availability(soup):
    """
    Concept:
    Availability tells us if the item is in stock.

    Amazon often stores this near id="availability".
    """

    # TODO: find element with id="availability"

    # TODO: return cleaned availability text

    pass


# -----------------------------
# Step 8: Extract bullet points
# -----------------------------

def get_bullets(soup):
    """
    Concept:
    Product pages usually have a feature list.

    Amazon often stores product details inside id="feature-bullets".

    We want to collect each bullet as text.
    """

    bullets = []

    # TODO: find the feature bullets section

    # Example:
    # bullet_section = soup.find(id="feature-bullets")

    # TODO: find all li tags inside that section

    # TODO: clean each bullet

    # TODO: ignore empty bullets

    return bullets


# -----------------------------
# Step 9: Build product dictionary
# -----------------------------

def parse_product(html):
    """
    Concept:
    This function controls the full parsing process.

    It turns raw HTML into organized product data.
    """

    soup = BeautifulSoup(html, "html.parser")

    product = {
        "title": get_title(soup),
        "price": get_price(soup),
        "rating": get_rating(soup),
        "review_count": get_review_count(soup),
        "availability": get_availability(soup),
        "bullets": " | ".join(get_bullets(soup))
    }

    return product


# -----------------------------
# Step 10: Save to CSV
# -----------------------------

def save_to_csv(product, filename):
    """
    Concept:
    A scraper/parser becomes more useful when the data is saved.
    """

    fieldnames = product.keys()

    # TODO: open CSV file

    # TODO: create DictWriter

    # TODO: write header

    # TODO: write product row

    pass


# -----------------------------
# Step 11: Print product nicely
# -----------------------------

def print_product(product):
    """
    Concept:
    Clean output helps us check if the parser worked.
    """

    print("-" * 50)
    print("Title:", product["title"])
    print("Price:", product["price"])
    print("Rating:", product["rating"])
    print("Reviews:", product["review_count"])
    print("Availability:", product["availability"])
    print("Bullets:", product["bullets"])
    print("-" * 50)


# -----------------------------
# Main program
# -----------------------------

def main():
    """
    Main flow:

    1. Load saved Amazon HTML
    2. Parse product data
    3. Print product data
    4. Save product data
    """

    # TODO: load HTML file

    # TODO: parse product

    # TODO: print product

    # TODO: save product to CSV

    pass


if __name__ == "__main__":
    main()