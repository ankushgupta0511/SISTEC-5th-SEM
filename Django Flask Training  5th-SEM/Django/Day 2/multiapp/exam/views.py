from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.




def testpappar(request):
    return HttpResponse('<h1>testpapar Page</h1>')

    

def result(request):
    return HttpResponse('<h1>result Page</h1>')

