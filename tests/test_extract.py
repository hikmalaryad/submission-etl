from utils.extract import (
    scrape_main,
    fetching_content,
    extract_product_data
)


def test_scrape_main():

    data = scrape_main(
        "https://fashion-studio.dicoding.dev/"
    )

    assert data is not None

    assert len(data) > 0


def test_fetching_content_error():

    result = fetching_content(
        "https://invalid-url-test.com"
    )

    assert result is None


def test_extract_product_data_error():

    result = extract_product_data(None)

    assert result is None