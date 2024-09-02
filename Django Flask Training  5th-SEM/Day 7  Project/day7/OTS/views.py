from django.shortcuts import render

# Create your views here.

from django.template import loader
from django.http import HttpResponse,HttpResponseRedirect
from OTS.models import *
import random


def welcome(request):
    template = loader.get_template('welcome.html')
    res = template.render()
    return HttpResponse(res)

def candidateRegistrationForm(request):
    res = render(request,'ragistration_form.html')
    return res

def candidateRegistration(request):
    pass

def loginView(request):
    pass
def candidateHome(request):
    pass
def testPaper(request):
    pass

def calculateTestResult(request):
    pass

def testResultHistory(request):
    pass

def showTestResult(request):
    pass

def logoutView(request):
    pass

