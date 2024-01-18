runserver:
	python manage.py runserver

newapp:
	python manage.py startapp mainapp

makemigrations:
	python manage.py makemigrations

migrate:
	python manage.py migrate

createsuperuser:
	python manage.py createsuperuser

fill_db:
	python manage.py fill_db

db_docker:
	docker compose up -d pg

test:
	python manage.py test

coverage:
	coverage run --source='.' manage.py test
	coverage report --omit=settings/asgi.py,setting/wsgi.py,manage.py,mainapp/management/* --fail-under=84
	coverage html --omit=settings/asgi.py,setting/wsgi.py,manage.py,mainapp/management/*