import pandas as pd

from utils.transform import transform_data


def test_transform_data():

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