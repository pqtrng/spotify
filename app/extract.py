import datetime
import pandas as pd
import requests

COLUMNS = ["song_name", "artist_name", "played_at", "time_stamp"]


def get_headers(token: str) -> dict:
    return {
        "Accept": "application/json",
        "Content-Type": "application/json",
        "Authorization": "Bearer {token}".format(token=token),
    }


def get_time_stamp(day: int = 1) -> int:
    start_date = datetime.datetime.now() - datetime.timedelta(days=day)
    return int(start_date.timestamp()) * 1000


def get_response(headers: dict, url: str, time_stamp: int) -> requests.Response:
    return requests.get(
        url=f"{url}{time_stamp}",
        headers=headers,
    )


def get_data_dict(res: requests.Response) -> dict:
    data = res.json()
    song_names = []
    artist_names = []
    played_at_list = []
    timestamps = []

    for song in data["items"]:
        song_names.append(song["track"]["name"])
        artist_names.append(song["track"]["album"]["artists"][0]["name"])
        played_at_list.append(song["played_at"])
        timestamps.append(song["played_at"][0:10])

    return {
        "song_name": song_names,
        "artist_name": artist_names,
        "played_at": played_at_list,
        "time_stamp": timestamps,
    }


def extract(token: str, url: str) -> pd.DataFrame:
    headers = get_headers(token=token)

    time_stamp = get_time_stamp()

    res = get_response(headers=headers, url=url, time_stamp=time_stamp)

    song_dict = get_data_dict(res)

    return pd.DataFrame(song_dict, columns=COLUMNS)


if __name__ == "__main__":
    pass
