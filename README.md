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


### Create a ASGI sevver to chat 

1. Install django channels
> pip install channels