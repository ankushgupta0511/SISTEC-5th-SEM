from django.urls import path
from exam import views

urlpatterns = [
    path('testpappar/',views.testpappar,name='testpappar'),
    path('result/',views.result,name='result')
    
]
