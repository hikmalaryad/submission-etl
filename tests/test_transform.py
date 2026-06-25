import pandas as pd
import pytest

from utils.transform import transform_data


def test_transform_data():
    """
    Memastikan proses transformasi
    berhasil dijalankan.
    """

    sample = {
        "Title": ["T-shirt 1"],
        "Price": ["$100.00"],
        "Rating": ["Rating: ⭐ 4.5 / 5"],
        "Colors": ["5 Colors"],
        "Size": ["Size: M"],
        "Gender": ["Gender: Men"],
        "Timestamp": ["2025-01-01"]
    }

    df = pd.DataFrame(sample)

    result = transform_data(df)

    assert not result.empty
    assert result.loc[0, "Price"] == 1600000.0
    assert result.loc[0, "Rating"] == 4.5
    assert result.loc[0, "Colors"] == 5
    assert result.loc[0, "Size"] == "M"
    assert result.loc[0, "Gender"] == "Men"


def test_transform_empty_dataframe():
    """
    Memastikan DataFrame kosong
    ditangani dengan benar.
    """

    df = pd.DataFrame()

    result = transform_data(df)

    assert result.empty


def test_transform_missing_column():
    """
    Memastikan kolom wajib yang hilang
    menghasilkan DataFrame kosong.
    """

    df = pd.DataFrame({
        "Title": ["T-shirt"],
        "Price": ["$100.00"]
    })

    result = transform_data(df)

    assert result.empty