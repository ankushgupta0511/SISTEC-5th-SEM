from django.urls import path
from mlapp.views import *

app_name = 'mlapp'

urlpatterns = [
    path('home/',home,name='home'),
    path('result/',result,name='result'),
]
