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



### How to run in local environment

Django management commands won’t automatically detect the settings file to use because the project settings file is not the default settings.py file. When running management commands, you need to indicate the settings module to use by adding a --settings option, as follows:

>python manage.py runserver --settings=educa.settings.local


Let’s run the local environment using the new settings structure. Make sure Redis is running or start the Redis Docker container in a shell with the following command:

>docker run -it --rm --name redis -p 6379:6379 redis

Run the following management command in another shell, from the project directory:

>python manage.py runserver --settings=educa.settings.local


### How to run in production mode 
>docker compose build
>docker compose up
> docker compose exec web python /code/cryptoclient/manage.py collectstatic