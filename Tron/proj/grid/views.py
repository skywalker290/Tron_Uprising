from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import *
from grid.models import *
from django.contrib.auth.models import User
from django.contrib.auth import *


from grid.models import user
# Create your views here.

def home(request):
    if(request.user.is_anonymous):
        return redirect("login")

    return render(request,'home.html')
    #return  HttpResponse("ths is homje");

def loginuser(request):
    if(request.method=="POST"):
        phone=request.POST.get('phone');
        password=request.POST.get('password');
        
        user=authenticate(username=phone,password=password);

        if(user is not None):
            login(request,user)
            return redirect("/")
        else:
            return redirect("login")


    return render(request,'login.html')
    #return  HttpResponse("ths is homje");

def register(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        password=request.POST.get('password')
        type=request.POST.get('radio')
        pincode=request.POST.get('pincode')

        cont=user(name=name,phone=phone,city=city,password=password,type=type,pincode=pincode)
        new_user=User.objects.create_user(username=phone,password=password)
        new_user.first_name=name;
        new_user.save()
        cont.save()
        return redirect("login");

        

    return render(request,'registration.html')
    #return  HttpResponse("ths is homje");



# def AUTH(phone,passwd):
#     query=user.objects.filter(phone=phone,password=passwd);
#     my_data=query.first();
#     print(my_data);
#     if(my_data):
#         return True;
#     else:
#         return False;

def logoutuser(request):
    logout(request)
    return redirect("login")

