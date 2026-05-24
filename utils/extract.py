import requests
import pandas as pd

from bs4 import BeautifulSoup
from datetime import datetime


HEADERS = {
    "User-Agent": (
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
        "AppleWebKit/537.36 (KHTML, like Gecko) "
        "Chrome/96.0.4664.110 Safari/537.36"
    )
}


def fetching_content(url):
    """
    Mengambil konten HTML dari website.
    """

    try:
        session = requests.Session()

        response = session.get(
            url,
            headers=HEADERS,
            timeout=10
        )

        response.raise_for_status()

        return response.content

    except requests.exceptions.RequestException as e:
        print(f"Error fetching website: {e}")

        return None


def extract_product_data(card):
    """
    Mengambil data product dari card HTML.
    """

    try:
        # title
        title_element = card.find(
            "h3",
            class_="product-title"
        )

        title = (
            title_element.text.strip()
            if title_element
            else "Unknown Product"
        )

        # price
        price_element = card.find(class_="price")

        price = (
            price_element.text.strip()
            if price_element
            else "Price Unavailable"
        )

        # product details
        product_details = card.find(
            "div",
            class_="product-details"
        )

        if not product_details:
            return None

        info_text = product_details.find_all("p")

        if len(info_text) < 4:
            return None

        rating = info_text[0].text.strip()
        colors = info_text[1].text.strip()
        size = info_text[2].text.strip()
        gender = info_text[3].text.strip()

        # timestamp
        timestamp = datetime.now().isoformat()

        # product dictionary
        product = {
            "Title": title,
            "Price": price,
            "Rating": rating,
            "Colors": colors,
            "Size": size,
            "Gender": gender,
            "Timestamp": timestamp
        }

        return product

    except Exception as e:
        print(f"Error extracting product: {e}")

        return None


def scrape_main(base_url, start_page=1, end_page=50):
    """
    Scraping seluruh halaman website.
    """

    products = []

    try:

        for page in range(start_page, end_page + 1):

            # page url
            if page == 1:
                url = base_url
            else:
                url = f"{base_url}page{page}"

            print(f"Scraping page {page}: {url}")

            # fetch html
            content = fetching_content(url)

            if not content:
                continue

            # parsing html
            soup = BeautifulSoup(
                content,
                "html.parser"
            )

            # ambil semua card
            cards = soup.find_all(
                "div",
                class_="collection-card"
            )

            # extract product
            for card in cards:

                product = extract_product_data(card)

                if product:
                    products.append(product)

        # dataframe
        return pd.DataFrame(products)

    except Exception as e:
        print(f"Error scraping main: {e}")

        return pd.DataFrame()