import sqlite3
import pandas as pd
import sqlalchemy
import sqlite3

from sqlalchemy import engine

QUERY = """
    CREATE TABLE IF NOT EXISTS tracks(
        song_name VARCHAR(200),
        artist_name VARCHAR(200),
        played_at VARCHAR(200),
        time_stamp VARCHAR(200),
        CONSTRAINT primary_key_constraint PRIMARY KEY (played_at)
    )
    """


def get_engine(location: str) -> sqlalchemy.engine:
    return sqlalchemy.create_engine(location)


def get_connection(database: str) -> sqlite3.Connection:
    return sqlite3.connect(database=database)


def get_cursor(connection: sqlite3.Connection) -> sqlite3.Cursor:
    return connection.cursor()


def create_database(cursor: sqlite3.Cursor, query: str = QUERY):
    cursor.execute(query)
    print("Opened database.")


def load(data: pd.DataFrame, location: str, database: str) -> None:
    engine = get_engine(location=location)
    connection = get_connection(database=database)
    cursor = get_cursor(connection=connection)
    
    create_database(cursor=cursor)
    
    try:
        data.to_sql("tracks", engine, index=False, if_exists="append")
    except:
        print("Data already exists in the databases")

    connection.close()
    print("Close database successfully.")
