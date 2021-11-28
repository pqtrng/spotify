from dotenv import load_dotenv
import os

# Local
from validate import validate
from extract import extract
from load import load

load_dotenv(".env")

if __name__ == "__main__":

    # Extract
    song_df = extract(token=os.environ["TOKEN"], url=os.environ["URL"])

    # Validate
    if validate(song_df):
        print("Data valid, proceed to Load stage")

    # Load
    load(
        data=song_df,
        location=os.environ["DATABASE_LOCATION"],
        database=os.environ["DATABASE"],
    )
