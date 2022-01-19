from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def homePageView(request): 
    return HttpResponse('Hello, World')

def djangoView(request):
    return HttpResponse('Hello, Django!')

def contactView(request):
    return HttpResponse('this is comming from contact View')

def about(request):
    return HttpResponse('this is comming from about views')

def skill(request):
    return HttpResponse('this is skill page')

def blogs(request):
    return HttpResponse('hello this is blog page')

def posts(request):
    return HttpResponse('this is posts pages')