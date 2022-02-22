release: python manage.py migrate --no-input
release: python manage.py makemigrations --no-input2
release: python manage.py migrate --no-input2
web gunicorn pizza.wsgi --log-file -