# Spotify

A data pipeline downloads recently played song from Spotify, saves that data in a SQLite database using Airflow.

## Prerequisites

- Python3
- Docker

## Step 1 — Grab the token

- Visit the Spotify and generate the token at [Get Recently Played Tracks Endpoint](https://developer.spotify.com/console/get-recently-played/)

- Put that token into the **.env** file

## Step 2 — Run the app

- Open terminal and run

```bash
docker-compose up -d --build
```

## Step 3 — Run task with Airflow

- Open Airflow at [localhost:8080](http://localhost:8080)
- Click on **spotify_dag** to open it
- Switch it on
- Then click on **Trigger DAG** to run
