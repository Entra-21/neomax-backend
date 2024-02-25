# neomax-backend

## Requirements:

- Python (version 3.8 or higher).
- pip

## First time running:

- Enter your virtual environment (how to create/activate a venv: https://docs.python.org/pt-br/3/library/venv.html)
- Run "pip install -r requirements.txt" (to install all dependencies)
- Run "python manage.py migrate" (to apply django's initial migration)
- Run "python manage.py loaddata drinks"
- Run "python manage.py createsuperuser"
- Run "python manage.py runserver"

Notes:

• Everytime you make/download updates to "core/models.py" you'll have to run "python manage.py migrate". You can keep track of those by running "python manage.py showmigrations".

• Some updates might include new libs, wich will be listed on "requirements.txt". Simply run "pip install -r requirements.txt" to download any new additions.

Links (run "python manage.py runserver"):

- http://127.0.0.1:8000/admin
- http://127.0.0.1:8000/api