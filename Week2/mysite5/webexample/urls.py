from django.conf.urls import url

from mysite5 import urls
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    ]