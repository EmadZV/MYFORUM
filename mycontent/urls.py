from django.contrib import admin
from django.urls import path
from . import views

app_name = 'mycontent'
urlpatterns = [
    path('', views.landing_page, name='landing_page'),
    path('newpost/', views.post_create, name='newpost'),
]
