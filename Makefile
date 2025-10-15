.PHONY: install run test docker-build docker-run

install:
	pip install -r requirements.txt

run:
	uvicorn app.main:app --host 0.0.0.0 --port 8080 --reload

test:
	pytest -q
