import pandas as pd
import pytest

from utils.load import (
    save_to_csv,
    save_to_google_sheets,
    save_to_postgresql
)

from unittest.mock import (
    MagicMock,
    mock_open,
    patch,
)


def test_save_to_csv(tmp_path):
    """
    Memastikan file CSV berhasil dibuat.
    """

    df = pd.DataFrame({
        "Title": ["T-shirt"]
    })

    filename = tmp_path / "test_products.csv"

    save_to_csv(
        df,
        filename
    )

    assert filename.exists()


def test_save_to_google_sheets():
    """
    Memastikan fungsi Google Sheets dapat dipanggil.
    """

    df = pd.DataFrame({
        "Title": ["T-shirt"]
    })

    try:

        save_to_google_sheets(
            df,
            "ETL Fashion Studio"
        )

    except Exception:

        pytest.fail(
            "save_to_google_sheets() menimbulkan exception."
        )


def test_save_to_postgresql():
    """
    Memastikan fungsi PostgreSQL dapat dipanggil.
    """

    df = pd.DataFrame({
        "Title": ["T-shirt"]
    })

    try:

        save_to_postgresql(
            df,
            "products_test"
        )

    except Exception:

        pytest.fail(
            "save_to_postgresql() menimbulkan exception."
        )