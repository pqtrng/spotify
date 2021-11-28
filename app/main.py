import sqlalchemy
import sqlite3
from dotenv import load_dotenv
import os

from validate import validate
from extract import extract

load_dotenv(".env")

if __name__ == "__main__":

    # Extract
    song_df = extract(token=os.environ["TOKEN"], url=os.environ["URL"])

    # Validate
    if validate(song_df):
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
