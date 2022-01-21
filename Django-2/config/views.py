from turtle import title
from django.http import HttpResponse
from django.shortcuts import render 

data= {
    'title' : 'Django Project-2',
    "p" : 'welcome to Django project', 
    'my' : ['yogesh', 19, 9843957012],
    'data' : [
            {'name':'yogesh khanal', 'phone': 9843957012},
            {'name': 'mahesh khanal', 'phone': 9876543210},
            {'name': 'kushal basnet', 'phone': 1234567890},
    ],
    'numbers': [10, 20, 30, 40, 50, 60, 70, 80],

}

def home(request):
    return render(request, 'index.html', data)

def aboutUs(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def service(request):
    return render(request, 'service.html')

# dynamic Routes
def courseDetail(request,id):
    return HttpResponse(id)