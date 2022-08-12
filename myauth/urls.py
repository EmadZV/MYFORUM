from django.urls import path
from myauth import views

urlpatterns = [
    path('login/', views.log_in, name='log_in')
]
