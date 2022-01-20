from django.urls import path
from .views import homePageView, djangoView,contactView,about, skill
from .views import *

urlpatterns = [
   path('home/', homePageView, name='home'),
   path('django/', djangoView, name='django'),
   path('contact/',contactView,name='contact'),
   path('about/',about,name='about'),
   path('skill/',skill,name='skill'),
   path('posts/',posts,name='posts'),
   path('blogs/',blogs,name='blogs'),
   
   # dynamic route : str: int: slug
   # path('blogs/<int:courseid>',courseDetail,name='blogs'), # ===> for intiger value
   # path('blogs/<str:courseid>',courseDetail,name='blogs'), # ===> for string value 
   # path('blogs/<slug:courseid>',courseDetail,name='blogs'), # ====> for slug value
   path('blogs/<courseid>',courseDetail,name='blogs'), # ====> if we are not sure about what kind of data is use then we can remove teh name such as int: str: slug

]