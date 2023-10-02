start:
	gunicorn goods_map.wsgi

dev:
	python3 manage.py runserver

migrate:
	python3 manage.py makemigrations
	python3 manage.py migrate

link:
	poetry run flake8

build:
	make migrate
	python3 manage.py collectstatic --noinput