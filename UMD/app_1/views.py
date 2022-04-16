from datetime import date,timedelta
from distutils.command.upload import upload
from email.policy import default
from django.shortcuts import render,HttpResponse
# from flask import current_app
from requests import session
from sqlalchemy import false
from .forms import FeedbackForm
from django.http import HttpResponse,HttpResponseRedirect
from app_1.models import Activemembers, Entry,DonationModel, FeedbackModel,MedicineStockModel, RequestModel
import random
from twilio.rest import Client
from django.db.models import Avg, Count, Min, Sum

from app_1.forms import FileForm

usersessions = {'login' : False,'userid' : ""}
adminsessions={'login' : False,'acid' : ""}

def dispose1(request):
    expired_date=date.today()+timedelta(days=60)
    MedicineStockModel.objects.filter(expiry_date__lte=expired_date).update(status="Expired")

def home_function(request):
    return render(request,'Home.html')

def monetory_function(request):
    return render(request,'monetory_donation.html')   
    
def donation_function(request) :
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    user=Entry.objects.filter(user_id=usersessions['userid']).first()
    if request.method=="POST":
        msg="Thanks for initiation"
        medicine_name=request.POST['medicine_name']
        medicine_quantity=request.POST['medicine_quantity']
        expiry_date=request.POST['expiry_date']
        phone=request.POST['phone']
        address=request.POST['address']
        if expiry_date == '':
                 return render(request, "medicine_donation.html",{'msg' : "please enter correct date"})
        b=DonationModel(status="pending",user_id=usersessions['userid'],medicine_name=medicine_name,medicine_quantity=medicine_quantity,expiry_date=expiry_date,pickup_address=address,phone_no=phone)
        b.save()
        return render(request, "medicine_donation.html",{'user':user,'msg' : msg})
    return render(request,"medicine_donation.html",{'user':user,'msg' : ""})

def request_function(request) :
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    user=Entry.objects.filter(user_id=usersessions['userid']).first()
    if request.method=='POST':
        medicine_name=request.POST['medicine_name']
        medicine_quantity=request.POST['medicine_quantity']
        purpose=request.POST['purpose']
        img=request.FILES['imag']
        RequestModel(status="pending",user_id=usersessions['userid'],medicine_name=medicine_name,medicine_quantity=medicine_quantity,purpose=purpose,image=img).save()
        return render(request, "medicine_request.html",{'user':user,'msg' : "request sent successfully"})
    return render(request,"medicine_request.html",{'user':user,'msg' : ""})

def feedback_function(request) :
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
   
    user=Entry.objects.filter(user_id=usersessions['userid']).first()
    if request.method=='POST':
        feedback=request.POST['feedb']
        rating=request.POST['rating']
        FeedbackModel(user_id=usersessions['userid'],feedback=feedback,rating=rating).save()
        return render(request,"profile.html",{'feedback' : "Thanks for your feedback",'user' : user})
    return render(request,"user_feedback.html",{'user' : user})

def register(request):
    return render(request,"register.html")

def show(request):
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})  
    user=Entry.objects.filter(user_id=usersessions['userid']).first()  
    d=DonationModel.objects.filter(user_id=usersessions['userid']).all()
    r=RequestModel.objects.filter(user_id=usersessions['userid']).all()
    return render(request,"show.html",{'d':d,'r':r,'user':user})

def enterotp(request):
    if request.method=='POST':
        otp=request.POST['otp'] 

def send(request):
    # if usersessions['login']==False :
    #     msg="Please Login"
    #     return render(request,'login.html',{'msg' : msg})
    if request.method=='POST':
        userid=request.POST['user_id']
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        adhaar=request.POST['adhaar']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        # img=request.FILES['imag']
        if Entry.objects.filter(user_id=userid).first() is not None :
            msg="UserID Already exists, please enter new ID"
            return render(request,'register.html',{'msg' : msg})
            
        global newentry
        global phonenum
        newentry=Entry(user_id=userid,name=name,address=address,email=email,phone=phone,adhaar=adhaar,pass1=pass1)
        phonenum=phone
        if pass1==pass2 : 
            global otpgot
            otpgot=otpget(phonenum)
            return render(request,"otp.html")      
        else:
            msg="Enter the same password "
            return render(request,"register.html",{'msg':msg})
    else:
         return HttpResponse("<h2>404-Error page not found !</h2>")

def otpfunc(request):

    otpentered=request.POST.get('otp')
    otp=int(otpentered)

    if(otpgot==otp):
        newentry.save()
        msg="You were added"
        return render(request,"login.html",{'msg':msg})
    else:
        msg="Wrong OTP"
        return render(request,"register.html",{'msg':msg})

def otpget(phonenum):
    str="+91"
    str=str+phonenum
    otp = random.randint(1000,9999)
    account_sid="AC45939b8689e9dbf036e8e6a2c045a750"
    auth_token ="344c3b6957a0d05faa18c75385c6bf82"
    client=Client(account_sid,auth_token)
    client.messages.create(
        body= f"Your OTP is {otp}",
        from_ = "+19107255048",
        to=str
        )
    return otp

def delete(request):
    adhaar=request.GET['adhaar']
    
    Entry.objects.filter(adhaar=adhaar).delete()
    return HttpResponseRedirect("show")

def adminedit(request):
    if  adminsessions['login']==True:
        user=Activemembers.objects.filter(acid=adminsessions['acid']).first()
        if request.method=='POST':
            name=request.POST['name']
            address=request.POST['address']
            email=request.POST['email']
            phone=request.POST['phone']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            img=request.FILES['imag']
            if pass1 != pass2:
                return render(request,"adminedit.html",{'msg':"please enter the passoword"})
            # if x:
            # img=request.FILES['imag']
            #     Activemembers.objects.filter(acid = adminsessions['acid']).update(name=name,address=address,email=email,phone=phone,pass1=pass1,image=img)
            # else:
            # Activemembers.objects.filter(acid = adminsessions['acid']).update(name=name,address=address,email=email,phone=phone,pass1=pass1)
            Activemembers.objects.filter(acid = adminsessions['acid']).update(name=name,address=address,email=email,phone=phone,pass1=pass1)
            
            user.image=img
            user.save(update_fields=['image'])
            return render(request,"adminedit.html",{'msg':"details edited successfully",'user' : user})
        else:
             return render(request,"adminedit.html",{'user':user})
    else:
        return render(request, 'Adminlogin.html')

def RecordEdited(request):
    if  usersessions['login']==True:
        user=Entry.objects.filter(user_id=usersessions['userid']).first()
        if request.method=='POST':
            name=request.POST['name']
            address=request.POST['address']
            email=request.POST['email']
            phone=request.POST['phone']
            pass1=request.POST['pass1']
            pass2=request.POST['pass2']
            img=request.FILES['imag']
            if pass1 != pass2:
                return render(request,"edit.html",{'msg':"please enter the passoword"})
            # x=request.POST['imag']
            # if x:
            # else:
            #     Entry.objects.filter(user_id = usersessions['userid']).update(name=name,address=address,email=email,phone=phone,pass1=pass1,image=img)
            #     Entry.objects.filter(user_id = usersessions['userid']).update(name=name,address=address,email=email,phone=phone,pass1=pass1)
            Entry.objects.filter(user_id = usersessions['userid']).update(name=name,address=address,email=email,phone=phone,pass1=pass1)
            if img is not None :
                user.image=img
                user.save(update_fields=['image'])
            
            return render(request,"profile.html",{'msg':"details edited successfully",'user' : user})
        else:
             return render(request,"edit.html",{'user':user})
    else:
        return render(request, 'login.html')
   
def login_user(request):
    if request.method=="POST":
        userid = request.POST.get('userid')
        pass1 = request.POST.get('pass1')

        # check if user has entered correct credentials
        # user = authenticate(adhaar=adhaar, pass1=pass1)
        user=Entry.objects.filter(user_id=userid,pass1=pass1).first()

        if user is not None:
            # A backend authenticated the credentials
            # login(request, user)            
            usersessions['login']=True
            usersessions['userid']=userid
            userinfo={'user' : user}
            return render(request, 'profile.html',userinfo)
        else:
            # No backend authenticated the credentials
            msg="Wrong Credentials"
            return render(request, 'login.html',{'msg':msg})
    return render(request, 'login.html')

def approvedonate(request) :
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    donate_id=request.GET['donate_id']
    DonationModel.objects.filter(donate_id=donate_id).update(status="Approve")
    medicine_name=DonationModel.objects.filter(donate_id=donate_id).first().medicine_name
    add=DonationModel.objects.filter(donate_id=donate_id).first().medicine_quantity
    expiry_date=DonationModel.objects.filter(donate_id=donate_id).first().expiry_date
    MedicineStockModel(medicine_name=medicine_name,medicine_quantity=add,expiry_date=expiry_date).save()  
    return HttpResponseRedirect("donations")

def rejectdonate(request) :
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    donate_id=request.GET['donate_id']
    DonationModel.objects.filter(donate_id=donate_id).update(status="Reject")
    return HttpResponseRedirect("donations")

def donations(request) :
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'AdminLogin.html',{'msg' : msg})
    data=DonationModel.objects.filter(status="pending")
    user=Activemembers.objects.filter(acid=adminsessions['acid']).first()
    return render(request,'Donationcheck.html',{'data':data,'user':user})
    
def adminlogin(request):
    if request.method=='POST':
        acid=request.POST.get('acid')
        pass1=request.POST.get('pass1')
        member=Activemembers.objects.filter(acid=acid,pass1=pass1).first()
        if member is not None:
            adminsessions['login']=True
            adminsessions['acid']=acid
            return render(request,'AdminProfile.html',{'user':member})
        else :
            msg="Wrong Credentials"
            return render(request,'AdminLogin.html',{'msg' : msg})

    return render(request,'AdminLogin.html')

def requests(request):
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    data=RequestModel.objects.filter(status="pending")
    user=Activemembers.objects.filter(acid=adminsessions['acid']).first()
    return render(request,'Requestcheck.html',{'data' : data ,'user':user})

def approverequest(request):
    if adminsessions['login']==False :
        return render(request,'AdminLogin.html',{'msg' : "please login"})
    dispose1(request)
    request_id=request.GET['request_id']
    medicine_name=RequestModel.objects.filter(request_id=request_id).first().medicine_name
    req_quantity=RequestModel.objects.filter(request_id=request_id,medicine_name=medicine_name).first().medicine_quantity

    cur=0
    for rows in MedicineStockModel.objects.filter(status="Usable",medicine_name=medicine_name):
        cur+=rows.medicine_quantity

    if cur<req_quantity:
        if cur!=0:
            MedicineStockModel.objects.filter(status="Usable",medicine_name=medicine_name).delete()
            status=str(cur) + " Passed and " + str(req_quantity-cur)+" Out of Stock"
            RequestModel.objects.filter(request_id=request_id).update(status=status)
        else :
            RequestModel.objects.filter(request_id=request_id).update(status="No Medicine Available")

    else :
        RequestModel.objects.filter(request_id=request_id).update(status="Approve Medicine")
        for rows in MedicineStockModel.objects.filter(status="Usable",medicine_name=medicine_name).order_by('expiry_date'):
            if rows.medicine_quantity<req_quantity:
                rows.delete()
                req_quantity-=rows.medicine_quantity
            else :
                upd=rows.medicine_quantity-req_quantity
                rows.medicine_quantity=upd
                rows.save(update_fields=['medicine_quantity'])
                break

    return HttpResponseRedirect("requests")

def rejectrequest(request) :
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'AdminLogin.html',{'msg' : msg})
    request_id=request.GET['request_id']
    RequestModel.objects.filter(request_id=request_id).update(status="Reject")
    return HttpResponseRedirect("requests")

def userlogout(request) :
    usersessions['userid']=""
    usersessions['login']=False
    return render(request,"Home.html")

def adminlogout(request):
    adminsessions['acid']=""
    adminsessions['login']=False
    return render(request,"Home.html")

def stocks(request):
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'AdminLogin.html',{'msg' : msg})
    dispose(request)
    user=Activemembers.objects.filter(acid=adminsessions['acid']).first()
    data=MedicineStockModel.objects.filter().all()
    return render(request,"stocks.html",{'data':data,'user':user})    

def profile(request):
    if(usersessions['login']):
        user=Entry.objects.filter(user_id=usersessions['userid']).first()
        userinfo={'user' : user}
        return render(request, 'profile.html',userinfo)
    else:
        return render(request,'login.html')
        
def adminprofile(request):
    if(adminsessions['login']):
        user=Activemembers.objects.filter(acid=adminsessions['acid']).first()
        return render(request,'AdminProfile.html' ,{'user':user})
    else:
        return render(request,'adminlogin.html')

def dispose(request):
    expired_date=date.today()+timedelta(days=60)
    MedicineStockModel.objects.filter(expiry_date__lte=expired_date).update(status="Expired")
    return HttpResponseRedirect('adminprofile')