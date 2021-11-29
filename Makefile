
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

down:
	docker-compose down
	
dev:
	docker-compose up -d --build

bash: dev
	docker exec -it airflow bash

requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

start:
	python app/etl.py