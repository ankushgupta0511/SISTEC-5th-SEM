from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required



# Create your views here.

@login_required(login_url = "/login/")
def add_receipe(request):
    
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')


        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        print(receipe_name )
        print(receipe_description )
        print(receipe_image )
        Receipe.objects.create(
            receipe_image = receipe_image,
            receipe_name = receipe_name,
            receipe_description = receipe_description)
        return redirect('/add-receipe/')
    return render(request,'add_receipe.html')






@login_required(login_url = "/login/")
def receipes(request):
    
    
    
    # if request.method == "POST":
    #     data = request.POST
    #     receipe_image = request.FILES.get('receipe_image')


    #     receipe_name = data.get('receipe_name')
    #     receipe_description = data.get('receipe_description')
    #     print(receipe_name )
    #     print(receipe_description )
    #     print(receipe_image )
    #     Receipe.objects.create(
    #         receipe_image = receipe_image,
    #         receipe_name = receipe_name,
    #         receipe_description = receipe_description)
        
        
    #     return redirect('/receipes/')
    
    
    queryset = Receipe.objects.all()


    if  request.GET.get('search'):
        queryset = queryset.filter(receipe_name__icontains = request.GET.get('search'))



    context = {
        "receipes":queryset
    }
        
    

    
    return render(request,'receipes.html',context)


@login_required(login_url = "/login/")
def update_receipe(request,id):
    print(id)
    queryset = Receipe.objects.get(id=id)
    # print(queryset)
    
    
    if request.method == "POST":
        data = request.POST
        receipe_image = request.FILES.get('receipe_image')
        receipe_name = data.get('receipe_name')
        receipe_description = data.get('receipe_description')
        print(receipe_name )
        print(receipe_description )
        print(receipe_image )

        queryset.receipe_name = receipe_name
        queryset.receipe_description = receipe_description

        if receipe_image:
            queryset.receipe_image = receipe_image
        
        queryset.save()
        return redirect('/receipes/')
        
    context = {
        "receipes":queryset
    }
    
    return render(request,'update_receipes.html',context)




@login_required(login_url = "/login/")
def delete_receipe(request,id):
    print(id)
    queryset = Receipe.objects.get(id=id)
    queryset.delete()
    return redirect('/receipes/')



def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        if not (User.objects.filter(username=username)):
            messages.info(request,'Invalid Login Credentials!!')
            return redirect('/login/')
        
        
        user = authenticate(username=username, password=password)
        if user is None:
            messages.info(request,'Invalid Password!!')
            return redirect('/login/')
        
        else:
            login(request,user)
            return redirect('/receipes/')
        

    return  render(request,'login.html')




def logout_page(request):
    logout(request)
    return redirect('/login/')




def register(request):
    
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')
        
        user = User.objects.filter(username = username)
        if user.exists():
            messages.info(request,'Username already exists!!')
            return redirect('/register/')
        
        user = User(
            
            first_name = first_name,
            last_name = last_name,
            username = username,
            
        )
        print(user)
        user.set_password(password)
        user.save()
        messages.info(request,'Account Created successfully!!')
        
        
        return redirect('/register/')
        
    return  render(request,'register.html')