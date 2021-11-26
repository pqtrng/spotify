import sqlalchemy
import pandas as pd
from sqlalchemy.orm import sessionmaker
import requests
import json
from datetime import datetime
import sqlite3
from config import AppConfig


if __name__ == "__main__":
    print(AppConfig.DATABASE_LOCATION)
