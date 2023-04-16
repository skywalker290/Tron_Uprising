from django.shortcuts import render,HttpResponse,redirect
from django.shortcuts import *
from grid.models import *
from django.contrib.auth.models import User
from django.contrib.auth import *
import datetime
# from .forms import ProductForm
from twilio.rest import Client



def send_sms(phone_number, message):
    TWILIO_ACCOUNT_SID = 'AC531f1718e64935ea8bdb30750606f345'
    TWILIO_AUTH_TOKEN = '4b75109c2ebb40cb0d49485181f65b76'
    TWILIO_PHONE_NUMBER = '+15752146590'
    client = Client(TWILIO_ACCOUNT_SID,TWILIO_AUTH_TOKEN)
    message = client.messages.create(
        to=phone_number,
        from_=TWILIO_PHONE_NUMBER,
        body=message
    )
    return message.sid

# def send_sms(to,message):
#     account_sid = "AC531f1718e64935ea8bdb30750606f345"
#     client = Client(account_sid, auth_token)
#     message = client.messages.create(
#     body="Hello from Twilio",
#     from_="+15752146590",
#     to="+919810030504"
#     )
#     print(message.sid)
# print(send_sms('+919810030504','inshalla bois played well'))




#home is the home posting function which respond according to the usertype if anonymous means no login 
#then send the userdata for displaying and further puroses
def home(request):
    #if user is anonymous we use a flag value for the website to know its anaonymous
    wsdata=workshop.objects.filter()
    print(request.POST.get('workshop_name'))
    if(request.user.is_anonymous):
        cont={
            'loggedin':False,
            'wsdata':wsdata
        }
        return render(request,'home.html',cont)
    #     return redirect("login")
    elif(request.POST.get('workshop_name')):
        wname=request.POST.get('workshop_name')
        wid=request.POST.get('workshop_id')
        book=workshopbook(wname=wname,wid=wid,pid=request.user)
        book.save()
    else:
        # print(request.user);
        userdata=user.objects.filter(phone=request.user)
        userdata=userdata.first()
        
        cont={
            'loggedin':True,
            'userdata':userdata,
            'wsdata':wsdata
        }
        return render(request,'home.html',cont)

    
    #return  HttpResponse("ths is homje");




#This function is for userlogin which basically gets values and auth.. 
#if matched then boom and save the userdata into a global varibale userdata
def loginuser(request):
    if(request.method=="POST"):
        phone=request.POST.get('phone');
        password=request.POST.get('password');
        
        uuser=authenticate(username=phone,password=password);

        if(uuser is not None):
            userdata=user.objects.filter(phone=phone)
            userdata=userdata.first()
            print(userdata)
            
            login(request,uuser)
            return redirect("/")
        else:
            return redirect("login")


    return render(request,'login.html')
    #return  HttpResponse("ths is homje");





#this is a register function in which regiter page post its request and we save it into the model named user 
#and create a user at the same time
def register(request):
    if(request.method=="POST"):
        name=request.POST.get('name')
        phone=request.POST.get('phone')
        city=request.POST.get('city')
        password=request.POST.get('password')
        type=request.POST.get('radio')
        pincode=request.POST.get('pincode')
        
        print(type);

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







#this is a simple logout function used to logout any existing logined user
def logoutuser(request):
    logout(request)
    return redirect("login")



#nearby function uses api in the javascript for which we send data of the user to 
#be forwarded to the api
def nearby(request):
    userdata=user.objects.filter(phone=request.user)
    userdata=userdata.first()
    cont={
        'loggedin':True,
        'userdata':userdata
    }
    return render(request,"maps.html",cont)


def pregister(request):
    if request.method == "POST"  :
        pname = request.POST.get('product-name')
        prange = request.POST.get('price-range')
        pimage = request.FILES['product-image']  # use request.FILES to access uploaded files
        pid=    gen_id()
        prod = product(pname=pname, sphone=request.user, price=prange, image=pimage,pid=pid)
        prod.save()

    userdata = user.objects.filter(phone=request.user)
    userdata = userdata.first()
    cont={
            'loggedin':True,
            'userdata':userdata
        }
    return render(request, "prodreg.html", cont)

def wsregister(request):
    if (request.method == "POST"):
        wname=request.POST.get('workshop-name')
        wimage=request.FILES['workshop-image']
        wabout=request.POST.get('workshop-about')
        wrange=request.POST.get('workshop-range')
        wcity=request.POST.get('workshop-city')
        wdatetime=request.POST.get('workshop-datetime')

        ws=workshop(wname=wname,wimage=wimage,wabout=wabout,wrange=wrange,wcity=wcity,wdatetime=wdatetime,wid=request.user)
        ws.save()
    
    userdata = user.objects.filter(phone=request.user)
    userdata = userdata.first()
    cont={
            'loggedin':True,
            'userdata':userdata
        }
    return render(request, "workshopreg.html", cont)




def wsbook(request):
    if(request.method=="POST" and (not request.user.is_anonymous)):
        wname=request.POST.get('workshop_name')
        wid=request.POST.get('workshop_id')
        book=workshopbook(wname=wname,wid=wid,pid=request.user)
        book.save()
    return redirect("home")


def gen_id():
    now = datetime.datetime.now()
    return now.strftime('%Y%m%d%H%M%S')

def shop(request):
    if(request.method=="POST"):
        if(request.user.is_anonymous):
            return redirect("login")
        else:
            orderid=gen_id()
            buyerid=request.user
            sellerid=request.POST.get('seller_id')
            product_name=request.POST.get('product_name')
            quantity=request.POST.get('quantity')
            pid=request.POST.get('product_id')
            order_date=datetime.date.today()
            req=order(orderid=orderid,buyerid=buyerid,sellerid=sellerid,
                      product_name=product_name,order_date=order_date,quantity=quantity
                      ,product_id=pid)
            req.save()
            message="ORDER RECIEVED:PRODUCT_NAME:%s QUANTITY:%s"%(product_name,quantity)
            phone=product.objects.filter(pid=pid)
            phone=phone.first()
            phone=phone.sphone;
            phone="+91"+phone;
            print(phone)
            # print(send_sms("+919548031969",message))

            return redirect("shop")
    else:
        userdata=user.objects.filter(phone=request.user)
        userdata=userdata.first()

        products=product.objects.filter()
        
        cont={
            'loggedin':True,
            'userdata':userdata,
            'products':products
        }
        return render(request,"ecom.html",cont)
    

def orders(request):
    ord=order.objects.filter(buyerid=request.user)
    userdata=user.objects.filter(phone=request.user)
    userdata=userdata.first()
    cont={
            'loggedin':True,
            'userdata':userdata,
            'orders':ord
        }
    return render(request,"orders.html",cont)

        
