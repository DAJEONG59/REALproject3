# ESG 1조, 장고

* 도르마무

##가상환경 조성 순서 (powershell실행)

* python -m venv venv
* venv\Scripts\activate
* python -m pip install "django~=4.1.0"
* python -m pip install -U pip
* python -m pip install wheel
* python manage.py makemigrations
* python manage.py migrate
* python -m pip install django-bootstrap5
* python manage.py runserver

