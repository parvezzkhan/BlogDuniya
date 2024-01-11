# BlogDuniya

# Django Blog Project

This is a simple Django blog project with MySQL database.

## Prerequisites

Make sure you have the following installed:

- Python (3.x)
- Pipenv
- MySQL (and the necessary development libraries)

## Setup

1. Clone the repository:

```bash
git clone https://github.com/your-username/django-blog.git

First Install Dependencies by using requirement.txt

## Now if you are using default database sqllite than no need to migrate

## I had used MySql Database :
Enter your database details in settings.py i already added mine
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Your Database name',
        'USER': 'Your Database User',
        'PASSWORD':'Your Database Password',
        'HOST':'127.0.0.1',
        'PORT':'3306'
    }
}


Now if you had added your database detail than do :
python manage.py makemigrations
python manage.py migrate

Now Runserver.....






