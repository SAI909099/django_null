mig:
	python3 manage.py makemigrations
	python3 manage.py migrate

user:
	python3 manage.py createsuperuser
#migdel:
#  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#  find . -path "*/migrations/*.pyc"  -delete
