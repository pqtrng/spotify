FROM puckel/docker-airflow:1.10.9

WORKDIR /usr/local/airflow/

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY .env .

COPY app ./app
