from django.contrib import admin
from django.urls import path
from . import views
app_name='admission'


urlpatterns = [

    path('courses/', views.courses, name='courses'),
    path('registeration/',views.registeration,name='registeration'),
    path('appdevelopment/', views.appdevelopment, name='appdevelopment'),
    path('webdesign/', views.webdesign, name='webdesign'),
    path('sendmail/',views.send_mail,name="mail"),
]
