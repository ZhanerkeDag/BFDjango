from django.conf.urls import url, include
from . import views

urlpatterns = [

    path('main/', views.index, name = 'index'),
    ]