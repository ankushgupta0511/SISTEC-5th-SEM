from django.shortcuts import render

from django.http import HttpResponse
# Create your views here.

def about(request):
    return render(request,'home/about.html')

def contect(request):
    return render(request,'home/contact.html')



def home(request):
    peoples = [
        {'name':'ankush','age':20},
        {'name':'monu','age':19},
        {'name':'vicky','age':2},
        {'name':'rocky','age':56}
    ]
    
    context = {
        'peoples':peoples
    }
    

    return render(request,'home/index.html',context)
    # return HttpResponse('<h1>Hy I am Django server.</h1>')
    

def success_page(request):
    return HttpResponse('<h1>Hy I am Django server. success</h1>')
    
    
