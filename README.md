# SkillUp blog priject

## Run in venv
```bash
pip install venv venv
.\venv\Scripts\activate.bat
(source venv/bin/activate)
```

## Install dependencies
```bash
pip install django
```
## Run server
```bash
django-admin startproject name_project 
python manage.py runserver
```
## Database initialisation
```bash 
python manage.py makemigrations
python manage.py migrate
```

## Create site administration
```bash
python manage.py createsuperuser
etc...
```
