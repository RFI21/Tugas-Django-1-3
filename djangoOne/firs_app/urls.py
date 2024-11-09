from django.urls import path
from firs_app import views

urlpatterns = [
    path('', views.index, name='index'),
]