from django.contrib import admin
from django.urls import path, include
from foods import views

urlpatterns = [
    path('', views.main_page, name="main_page")
]
