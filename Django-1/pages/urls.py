from django.urls import path
from .views import homePageView, djangoView,contactView,about, skill
from .views import *

urlpatterns = [
   path('home/', homePageView, name='home'),
   path('django/', djangoView, name='django'),
   path('contact/',contactView,name='contact'),
   path('about/',about,name='about'),
   path('skill/',skill,name='skill'),

]