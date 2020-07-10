from django.contrib import admin
from django.urls import path
from . import views
from django.conf.urls import url
app_name='students'


urlpatterns = [

    path('signup/', views.signup, name='signup'),
    path('login/', views.login_view, name='login'),
    path('studentprofile/', views.student_profile, name='studentprofile'),
    path('logout/', views.logout_view, name='logout'),
    url(r'^update/(?P<pk>\d+)$',views.update,name='update'),

]
