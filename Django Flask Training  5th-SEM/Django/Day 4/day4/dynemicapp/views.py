from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse

# Create your views here.


def testpapar(request):
    
    ques = "who developed python?"
    a='dennis richi'
    b='nikhil'
    c='aman'
    d ='monu'
    
    context = {
      'ques':ques,
      'options':[a,b,c,d]
    }
   
    
    
    
    
    template = loader.get_template('index.html')
    res = template.render(context,request)
    return  HttpResponse(res)

