import pandas as pd
import pytest

from utils.extract import (
    scrape_main,
    fetching_content,
    extract_product_data
)


def test_scrape_main():
    """
    Memastikan proses scraping berhasil
    menghasilkan DataFrame yang tidak kosong.
    """

    data = scrape_main(
        "https://fashion-studio.dicoding.dev/"
    )

    assert isinstance(data, pd.DataFrame)
    assert not data.empty


def test_fetching_content_error():
    """
    Memastikan URL yang tidak valid
    mengembalikan None.
    """

    result = fetching_content(
        "https://invalid-url-test.com"
    )

    assert result is None


def test_extract_product_data_error():
    """
    Memastikan input None
    ditangani dengan baik.
    """

    result = extract_product_data(None)

    assert result is None