import datetime
import pandas as pd


def check_empty(df: pd.DataFrame) -> bool:
    if df.empty:
        print("No songs downloaded. Finishing execution.")
        return False
    # print("DataFrame is not empty")
    return True


def check_data_unique(df: pd.DataFrame):
    if pd.Series(df["played_at"]).is_unique:
        # print("All data is unique.")
        pass
    else:
        raise Exception("Primary Key Check is violated.")


def check_nulls(df: pd.DataFrame):
    if df.isnull().values.any():
        raise Exception("Null values found.")

    # print("There is no null value.")


def check_timestamp(df: pd.DataFrame):
    yesterday = datetime.datetime.now() - datetime.timedelta(days=1)
    yesterday = yesterday.replace(hour=0, minute=0, second=0, microsecond=0)

    time_stamps = df["time_stamp"].tolist()

    for time_stamp in time_stamps:
        if datetime.datetime.strptime(time_stamp, "%Y-%m-%d") != yesterday:
            raise Exception(
                "At least one of the returned songs does not come from within the last 24 hours."
            )

    return True


def validate(df: pd.DataFrame) -> bool:
    # empty check
    if check_empty(df):

        # unique check
        check_data_unique(df)

        # null check
        check_nulls(df)

        # timestamp check
        # return check_timestamp(df)
        return True
