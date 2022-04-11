serve:
	python3.8 manage.py runserver

migrations:
	python3.8 manage.py makemigrations

migrate:
	python3.8 manage.py migrate

freeze:
	pip freeze > requirements.txt		

test:
	python manage.py test