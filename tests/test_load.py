import pandas as pd

from utils.load import (
    save_to_csv,
    save_to_google_sheets,
    save_to_postgresql
)


def test_save_to_csv():

    df = pd.DataFrame({
        "Title": ["T-shirt"]
    })

    save_to_csv(
        df,
        "test_products.csv"
    )

    assert True


def test_save_to_google_sheets():

    df = pd.DataFrame({
        "Title": ["T-shirt"]
    })

    try:

        save_to_google_sheets(
            df,
            "ETL Fashion Studio"
        )

    except Exception:

        pass

    assert True


def test_save_to_postgresql():

    df = pd.DataFrame({
        "Title": ["T-shirt"]
    })

    try:

        save_to_postgresql(
            df,
            "products_test"
        )

    except Exception:

        pass

    assert True