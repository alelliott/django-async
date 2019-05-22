## Boilerplate Django Project with PostgreSQL, Channels 2, Redis, RabbitMQ, and Celery  
This project serves as a starting point for creating real-time Django projects that run on a PostgreSQL database.  
Channels 2 adds an asynchronous layer on top of Django, enabling handing of connections and sockets. Channels uses Redis as its backing store.  
Celery is used for task queuing/scheduling and is configured to use RabbitMQ as its messaging queue.  

![alt text](https://user-images.githubusercontent.com/26307290/58209131-afa74800-7ca3-11e9-84f7-04ba1d969b1b.png)

Start your project using:  
```
django-admin startproject {project_name} --extension py,yml,json --name README.md,Dockerfile,sample.env --template=https://github.com/alelliott/django-async/archive/master.zip
```

## Project Template Overview  

```
<{{ project_name }}>
      └── applications
          ├── dashboard
          ├── example_task
      └── <{{ project_name }}>
          ├── __init__.py
          ├── asgi.py
          ├── celery.py
          └── settings
            ├── base.py
            ├── local.py
            ├── production.py
            └── staging.py
          ├── urls.py
          └── wsgi.py
      ├── manage.py
      ├── README.md
      ├── requirements.txt
      └── sample.env
```  

Django project settings are located in the `<{{ project_name }}>/settings` folder.  
Two example/boilerplate Django applications are included: `dashboard` and `example_task`.  

## Docker - Quick Start  

1. Make sure you have `docker` and `docker-compose` installed on your system
2. Create a local copy of the env file: `cp sample.env .env` 
3. Run `docker-compose up --build` to quickly bring up `daphne`, `postgres`, `rabbitmq`, and `redis` preconfigured and bound to their default ports.

Once built, migrate and create a superuser with the following commands:  
`docker-compose exec web python manage.py migrate`  
`docker-compose exec web python manage.py createsuperuser`  

## Local Setup  

Initialize Postgres by running the following commands from within the Postgres
interactive terminal. Make sure to replace the parameters within brackets with
your own settings:

1. `psql` to start interactive Postgres terminal.  
2. `CREATE USER {username} WITH PASSWORD {password};`  
3. `CREATE DATABASE {project_name} WITH OWNER {username};`  
4. Quit psql terminal and return to shell to run the following:
5. `virtualenv .env_py3` create python virtual environment  
6. `source .env_py3/bin/activate` activate virtual environment  
7. `pip install -r requirements.txt`  install python dependencies  
8. `cp sample.env .env` copy sample .env file, change service HOSTS to `localhost`     
9. Edit `.env` with updated settings, ensure database variables are updated for local db   
10. `python manage.py migrate`  initialize database tables   
11. `python manage.py createsuperuser` create admin user  
12. `python manage.py runserver` starts local webserver  
13. `rabbitmq-server` starts RabbitMQ (add ` -detached` to run in the background)  
14. `celery worker -A {project_name} -l info` start celery workers  

To shutdown RabbitMQ, run `rabbitmqctl stop`  

## Adding Apps
Django Applications for the project are stored in the `applications` folder and 
the Django project is preconfigured to reference apps in this folder. To add an
app:

1. `cd applications`  
2. `python ../manage.py startapp {appname}` to create a Django app in the applications directory  
3. Within the newly created app folder, open `apps.py` and add "applications" before the name of your app:  
    ```
    name = 'applications.{appname}'
    ```
4. Open `base.py` from the main project's settings folder and add the name of the app to the PROJECT_APPS list.  