from django.urls import path
from myweb import views

urlpatterns = [
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    
    path('python/',views.python,name='python'),
    path('django/',views.django,name='django'),
]
