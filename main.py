import pandas as pd

from utils.extract import scrape_main
from utils.transform import transform_data

from utils.load import (
    save_to_csv,
    save_to_google_sheets,
    save_to_postgresql
)


BASE_URL = (
    "https://fashion-studio.dicoding.dev/"
)


def main():

    # extract
    raw_data = scrape_main(BASE_URL)

    # dataframe
    df = pd.DataFrame(raw_data)

    # transform
    clean_df = transform_data(df)

    # load ke csv
    save_to_csv(clean_df)

    # load ke google sheets
    save_to_google_sheets(
        clean_df,
        "ETL Fashion Studio"
    )

    # load ke postgresql
    save_to_postgresql(clean_df)

    print(clean_df.head())


if __name__ == "__main__":
    main()