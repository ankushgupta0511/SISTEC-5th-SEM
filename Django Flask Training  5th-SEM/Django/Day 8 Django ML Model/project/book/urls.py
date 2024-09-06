from django.urls import path
from book import views
urlpatterns = [
    path('',views.home,name='home'),
    path('store/',views.store,name='store'),
    path('get/',views.get,name='get')
]
