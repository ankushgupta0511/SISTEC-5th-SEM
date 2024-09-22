from django.contrib import admin
from django.urls import path,include
from healthprediction.views import DiseasePredict 
urlpatterns = [
    path('', DiseasePredict.as_view(),name='disease-prediction'),
]
