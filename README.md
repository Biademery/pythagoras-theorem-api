# Installing

```sh
python3 -m venv venv
pip install -r requirements.txt
python3 manage.py migrate
python3 manage.py createsuperuser --username admin --email admin@mail.com
python3 manage.py runserver
```