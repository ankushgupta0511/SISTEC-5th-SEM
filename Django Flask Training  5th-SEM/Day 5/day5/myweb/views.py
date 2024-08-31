from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader


# Create your views here.
def home(request):
    template = loader.get_template('home.html')
    res = template.render()
    return HttpResponse(res)



def about(request):
    template = loader.get_template('about.html')
    res = template.render()
    return HttpResponse(res)



def python(request):
    template = loader.get_template('python.html')
    res = template.render()
    return HttpResponse(res)



def django(request):
    template = loader.get_template('django.html')
    res = template.render()
    return HttpResponse(res)






