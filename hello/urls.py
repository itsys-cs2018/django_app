'''
Created on 2018/10/24

@author: stomo
'''
from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
]
