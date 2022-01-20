
from django.contrib import admin
from django.urls import path, include 
from config import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('about-us/', views.aboutMe),
    path('courses/', views.courses),
 
    # Dynamic Routes
    # dynamic route : str: int: slug
   # path('blogs/<int:courseid>',courseDetail,name='blogs'), # ===> for intiger value
   # path('blogs/<str:courseid>',courseDetail,name='blogs'), # ===> for string value 
   # path('blogs/<slug:courseid>',courseDetail,name='blogs'), # ====> for slug value
   path('course/<id>', views.courseDetail), # ====> if we are not sure about what kind of data is use then we can remove teh name such as int: str: slug
   
]