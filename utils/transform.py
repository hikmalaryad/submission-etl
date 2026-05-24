import pandas as pd


def transform_data(df):
    """
    Membersihkan dan mentransformasi data hasil scraping.
    """

    try:

        # validasi dataframe
        if df is None or df.empty:
            raise ValueError(
                "DataFrame kosong atau None"
            )

        # copy dataframe
        df = df.copy()

        # validasi kolom wajib
        required_columns = [
            "Title",
            "Price",
            "Rating",
            "Colors",
            "Size",
            "Gender",
            "Timestamp"
        ]

        for column in required_columns:

            if column not in df.columns:

                raise ValueError(
                    f"Kolom {column} tidak ditemukan"
                )

        # hapus duplicate
        df = df.drop_duplicates()

        # hapus null
        df = df.dropna()

        # hapus unknown product
        df = df[
            df["Title"] != "Unknown Product"
        ]

        # hapus price unavailable
        df = df[
            df["Price"] != "Price Unavailable"
        ]

        # clean price
        df["Price"] = (
            df["Price"]
            .str.replace(
                "$",
                "",
                regex=False
            )
            .astype(float)
            * 16000
        )

        # hapus invalid rating
        df = df[
            ~df["Rating"].str.contains(
                "Invalid",
                na=False
            )
        ]

        # clean rating
        df["Rating"] = (
            df["Rating"]
            .str.extract(
                r"(\d+\.\d+)"
            )[0]
            .astype(float)
        )

        # clean colors
        df["Colors"] = (
            df["Colors"]
            .str.extract(
                r"(\d+)"
            )[0]
            .astype(int)
        )

        # clean size
        df["Size"] = (
            df["Size"]
            .str.replace(
                "Size: ",
                "",
                regex=False
            )
            .str.strip()
        )

        # clean gender
        df["Gender"] = (
            df["Gender"]
            .str.replace(
                "Gender: ",
                "",
                regex=False
            )
            .str.strip()
        )

        # convert timestamp
        df["Timestamp"] = pd.to_datetime(
            df["Timestamp"]
        )

        # reset index
        df.reset_index(
            drop=True,
            inplace=True
        )

        return df

    except Exception as e:

        print(
            f"Error transform data: {e}"
        )

        return pd.DataFrame()