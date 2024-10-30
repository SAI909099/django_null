mig:
	python3 manage.py makemigrations
	python3 manage.py migrate


#migdel:
#  find . -path "*/migrations/*.py" -not -name "__init__.py" -delete
#  find . -path "*/migrations/*.pyc"  -delete
