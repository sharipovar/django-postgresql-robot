## Установка

1. Установить [PostgreSQL](https://www.postgresql.org/download/)
2. Установить [Python](https://www.python.org/downloads/)
3. Установить [Django](https://www.djangoproject.com/download/)
   ```
   pip install Django --upgrade
   ```
4. Установить [psycopg2](https://www.psycopg.org/install/)
   ```
   pip install psycopg2 --upgrade
   ```
## Django

1. Создать проект Django:
   ```
   django-admin startproject mysite
   ```

   подробнее описано здесь: https://docs.djangoproject.com/en/4.1/intro/tutorial01/
2. Создать таблицы для проекта в PostgreSQL:
   ```
   python manage.py migrate
   ```

   подробнее описано здесь: https://docs.djangoproject.com/en/4.1/ref/databases/#postgresql-notes
3. Создать приложение Django:
   ```
   python manage.py startapp blog
   ```

   подробнее здесь: https://docs.djangoproject.com/en/4.1/intro/tutorial01/#creating-the-polls-app