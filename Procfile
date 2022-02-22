release: python manage.py migrate --no-input
release: python3 install -r requirements.txt 
web gunicorn pizza.wsgi --log-file -