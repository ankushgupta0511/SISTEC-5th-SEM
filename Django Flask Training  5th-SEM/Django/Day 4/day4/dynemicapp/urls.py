from django.urls import path
from dynemicapp import views


urlpatterns = [
    path('',views.testpapar,name='testpapar'),
]
