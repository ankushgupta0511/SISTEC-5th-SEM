from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
import joblib

# Create your views here.



def home(request):
    template = loader.get_template('home.html')
    return HttpResponse(template.render())



def result(request):
    cls = joblib.load('glassmlmodel.sav')
    lis = []
    lis.append(float(request.GET['RI']))
    lis.append(float(request.GET['Na']))
    lis.append(float(request.GET['Mg']))
    lis.append(float(request.GET['Al']))
    lis.append(float(request.GET['Si']))
    lis.append(float(request.GET['K']))
    lis.append(float(request.GET['Ca']))
    lis.append(float(request.GET['Ba']))
    lis.append(float(request.GET['Fe']))

    print(lis)
    ans = cls.predict([lis])
    
    # template = loader.get_template('result.html')
    return render(request,'result.html',{'ans':ans,'lis':lis})


