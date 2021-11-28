import sqlalchemy
from sqlalchemy.orm import sessionmaker
import requests
import json
import pandas as pd
import datetime
import sqlite3
from dotenv import load_dotenv
import os

from utils import check_if_valid_data

load_dotenv(".env")

if __name__ == "__main__":

    # Extract
    headers = {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=os.environ["TOKEN"]),
    }

    today = datetime.datetime.now()
    yesterday = today - datetime.timedelta(days=1)
    yesterday_unix_timestamp = int(yesterday.timestamp()) * 1000

    r = requests.get(
        url="https://api.spotify.com/v1/me/player/recently-played?after={time}".format(
            time=yesterday_unix_timestamp
        ),
        headers=headers,
    )

    data = r.json()

    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    song_dict = {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "time_stamp": timestamps,
    }

    song_df = pd.DataFrame(
        song_dict, columns=["song_name", "artist_name", "played_at", "time_stamp"]
    )

    # Validate
    if check_if_valid_data(song_df):
        print("Data valid, proceed to Load stage")

    # Load
    engine = sqlalchemy.create_engine(os.environ["DATABASE_LOCATION"])
    connection = sqlite3.connect("tracks.sqlite")
    cursor = connection.cursor()

    sql_query = """
    CREATE TABLE IF NOT EXISTS tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        time_stamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """

    cursor.execute(sql_query)

    print("Opened database.")

    try:
        song_df.to_sql("tracks", engine, index=False, if_exists="append")
    except:
        print("Data already exists in the databases")

    connection.close()
    print("Close database successfully.")
