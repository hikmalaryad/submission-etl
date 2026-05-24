import os
import pickle

import gspread
import pandas as pd

from sqlalchemy import create_engine

from google.auth.transport.requests import Request

from google_auth_oauthlib.flow import (
    InstalledAppFlow
)


def save_to_csv(
    df,
    filename="products.csv"
):
    """
    Menyimpan data ke CSV.
    """

    try:

        df.to_csv(
            filename,
            index=False
        )

        print(
            f"Data berhasil disimpan ke {filename}"
        )

    except Exception as e:

        print(
            f"Error save CSV: {e}"
        )


def save_to_google_sheets(
    df,
    spreadsheet_name
):
    """
    Menyimpan data ke Google Sheets.
    """

    try:

        SCOPES = [
            "https://www.googleapis.com/auth/spreadsheets",
            "https://www.googleapis.com/auth/drive"
        ]

        creds = None

        if os.path.exists(
            "token.pickle"
        ):

            with open(
                "token.pickle",
                "rb"
            ) as token:

                creds = pickle.load(token)

        if not creds or not creds.valid:

            if (
                creds
                and creds.expired
                and creds.refresh_token
            ):

                creds.refresh(
                    Request()
                )

            else:

                flow = (
                    InstalledAppFlow
                    .from_client_secrets_file(
                        "google-sheets-api.json",
                        SCOPES
                    )
                )

                creds = (
                    flow.run_local_server(
                        port=0
                    )
                )

            with open(
                "token.pickle",
                "wb"
            ) as token:

                pickle.dump(
                    creds,
                    token
                )

        client = gspread.authorize(
            creds
        )

        spreadsheet = client.open(
            spreadsheet_name
        )

        worksheet = spreadsheet.sheet1

        worksheet.clear()

        worksheet.update(
            [df.columns.values.tolist()]
            + df.values.tolist()
        )

        print(
            "Data berhasil disimpan ke Google Sheets"
        )

    except Exception as e:

        print(
            f"Error Google Sheets: {e}"
        )


def save_to_postgresql(
    df,
    table_name="products"
):
    """
    Menyimpan data ke PostgreSQL.
    """

    try:

        DB_USER = "postgres"
        DB_PASSWORD = "postgres"
        DB_HOST = "localhost"
        DB_PORT = "5432"
        DB_NAME = "fashion_db"

        engine = create_engine(
            f"postgresql+psycopg2://"
            f"{DB_USER}:{DB_PASSWORD}"
            f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
        )

        df.to_sql(
            table_name,
            engine,
            if_exists="replace",
            index=False
        )

        print(
            "Data berhasil disimpan ke PostgreSQL"
        )

    except Exception as e:

        print(
            f"Error PostgreSQL: {e}"
        )