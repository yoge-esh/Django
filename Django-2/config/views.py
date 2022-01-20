from turtle import title
from django.http import HttpResponse
from django.shortcuts import render 

data= {
    'title' : 'Django Project-2',
    "p" : 'welcome to Django project', 
    'my' : ['yogesh', 19, 9843957012],
}

def home(request):
    return render(request, 'index.html', data)
def aboutMe(request):
    return HttpResponse('Welcome to Django project -2')

def courses(request):
    return HttpResponse('this is a course page')

# dynamic Routes
def courseDetail(request,id):
    return HttpResponse(id)