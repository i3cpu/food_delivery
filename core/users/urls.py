from django.urls import path, include
from . import views

urlpatterns = [
    path('/login',views.login, name='login'),
    path('/registration',views.registration, name='registration'),
    path('/userprofile',views.userprofile, name='userprofile'),
    path('/logout',views.logout, name='logout'),

]

