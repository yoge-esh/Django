1. create a virtual environment 

-> python -m venv venv


2. activate venv 

source venv/bin/activate  ---> linux / mac
#windows users  before activating make sure to run this command in the powershell
#Set-ExecutionPolicy -Scope CurrentUser -ExecutionPolicy Unrestricted

-> source(venv)\Scripts\activate ---> windows


3. installing Django

-> pip install django~=3.2.8


4. save requirements.txt 

-> pip freeze > requirements.txt


5. install requirements.txt

-> pip install -r requirements.txt


6. create Django project

-> django-admin startproject config . ---> notice the dot at the end of the project name

### Django Project Structure ###

├── config
    │
    ├── __init__.py
    |
    ├── asgi.py -> helps to run Asynchronous Server Gateway Interface Apps
    │
    ├── settings.py -> controls our project's settings
    │
    ├── urls.py -> tells Django which pages to build in respsonse to a browser or URL request
    │
    └── wsgi.py -> Web Server Gateway Interface, helps Django server our eventual web pages.
│   
└── manage.py  -> used to execute various Django commands such as running the local web server or creating a new app.


7. Remove the warnings

-> python manage.py migrate


8. Start the Development server

-> python manage.py runserver


9. Create an App ---> Django uses the concept of projects and apps to keep code clean and readable. A single Django project contains one or more apps within it that all work together to power a web application.
Create our first App

-> python manage.py startapp pages

### Django App Structure ###
(helloworld) $ tree

├── pages
    │
    ├── __init__.py
    │
    ├── admin.py -> configuration file for the built-in Django Admin app
    │
    ├── apps.py -> configuration file for the app itself
    │   
    ├── migrations ->migrations/ keeps track of any changes to our models.py file so our database and models.py stay in sync
        │
        └── __init__.py
    │
    ├── models.py -> where we define our database models which Django automatically translates into database tables
    │
    ├── tests.py -> for our app-specific tests
    │
    └── views.py -> where we handle the request/response logic for our web app


10. Add our new pages app to Django project
# config/settings.py
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
 ->   'pages', # add app here
]

URLs, Views, Models, Templates
HTTP request/response cycle.
When you type in a URL (HTTP request), such as https://www.example.com, the first thing that happens within our Django project is a URLpattern is found that matches the homepage.
The URLpattern specifies a view which then determines the content for the page (usually from a database model) and then ultimately a template for styling and basic logic. The end result is sent back to the user as an HTTP response.

# Django request/response cycle
URL -> View -> Model (typically) -> Template

views -> determine what content is displayed on a given page
urls -> determines where that content is going
model -> cotains the content from the database
template -> provides styling for the data

11. Update the view.py
pages/views.py
-> from django.http import HttpResponse

-> def homePageView(request):

    -> return HttpResponse('Hello, World!')


12. Upadate out projectsurls.py
# config/urls.py

-> from django.contrib import admin

-> from django.urls import path, include # new

-> urlpatterns = [

    -> path('admin/', admin.site.urls),
    
    -> path('', include('pages.urls')), # new
]

13. Restart our Django Server
-> python manage.py runserver
