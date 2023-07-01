from django.urls import path
from . import views

urlpatterns = [
    path('', views.index)          # Homepage of the web application
]