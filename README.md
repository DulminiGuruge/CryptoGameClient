## Django based front end created to communicate with the flask server for crypto mining game

### Create the environment

> pipenv install django

> pipenv shell

> django-admin startproject cryptoclient

> python manage.py migrate

> python manage.py runserver

### Create the login

1. Create templates/registration and login.html inside it.
2. Add  "DIRS": [BASE_DIR / "templates"] to TEMPLATES  section in settings.py.
3. Specify where to redirect the user upon a successful login using the LOGIN_REDIRECT_URL setting.
4. Run  python manage.py runserver
5. http://127.0.0.1:8000/accounts/login/


### Create a ASGI server to chat 

1. Install django channels

> pip install channels

> pip install Daphne


### How to connect to google cloud PostgreSQL from the local django framework app for testing

Visit below links

1. https://stackoverflow.com/questions/50132394/how-do-you-connect-to-google-cloud-postgresql-via-django-framework

2. https://cloud.google.com/sql/docs/postgres/configure-ssl-instance