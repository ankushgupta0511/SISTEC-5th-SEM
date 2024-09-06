from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from book.models import BookD

# Create your views here.

def home(request):
    return render(request,'home.html')

def store(request):
    if request.method == 'POST':
       bname = request.POST['bname']
       bamount = request.POST['bamount']
       print(bname,bamount)
       bk = BookD(bname=bname,bprice=bamount)
       bk.save()
    return render(request,'store.html')



def get(request):
    queryset = BookD.objects.all()
    return render(request,'get.html',{'queryset':queryset})

