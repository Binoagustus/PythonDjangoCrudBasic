# PythonDjangoCrudBasic
Basic python Crud Application

Django Project creation and running steps
1. Create a project using
a. **django-admin startproject <projectname>**
b. **cd <projectname>** to go inside project
2. Create an application using
a. **python manage.py startapp <appname>**
3. After creation of urls, models and serializers, and views
4. Create migrations using
a. **python manage.py makemigrations <appname>**
b. **python manage.py migrate**
5. After the tables have been created in db run the application using
**python manage.py runserver**
