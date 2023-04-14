from django.shortcuts import render,HttpResponse,redirect
from grid.models import user
# Create your views here.

def home(request):
    return render(request,'home.html')
    #return  HttpResponse("ths is homje");

def login(request):
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
        cont.save()
        redirect("login")

        

    return render(request,'registration.html')
    #return  HttpResponse("ths is homje");
