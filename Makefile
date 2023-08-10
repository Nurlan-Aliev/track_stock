start:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

link:
	poetry run flake8

static:
	python3 manage.py collectstatic

build:
	make migrate
	make static