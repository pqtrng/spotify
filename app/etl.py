from dotenv import load_dotenv
import os, sys

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), os.path.pardir))
)

# Local
from app.validate import validate
from app.extract import extract
from app.load import load

load_dotenv(".env")


def etl():
    # Extract
    song_df = extract(token=os.environ["TOKEN"], url=os.environ["URL"])
    print("Finish extracting data!")
    print(song_df.head())

    # Validate
    if validate(song_df):
        print("Data valid, proceed to Load stage")

    # Load
    load(
        data=song_df,
        location=os.environ["DATABASE_LOCATION"],
        database=os.environ["DATABASE"],
    )


if __name__ == "__main__":
    etl()
