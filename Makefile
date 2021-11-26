
ifneq (,$(wildcard ./.env))
    include .env
    export
endif

clean:
	docker rm $(CONTAINER_NAME) -vf || true
	docker image rm $(CONTAINER_IMAGE) -f || true
	docker image ls

down:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down
dev:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

bash:
	docker exec -it $(CONTAINER_NAME) bash

log:
	docker logs $(CONTAINER_NAME) -f

requirements:
	pip install --upgrade pip
	pip install -r requirements.txt

start:
	python app/main.py