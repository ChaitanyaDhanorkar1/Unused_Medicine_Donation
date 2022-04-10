from django.shortcuts import render,HttpResponse
from sqlalchemy import false
from .forms import FeedbackForm
from django.http import HttpResponse,HttpResponseRedirect
from app_1.models import Activemembers, Entry,DonationModel,MedicineStockModel, RequestModel
import random
from twilio.rest import Client

usersessions = {'login' : False,'userid' : ""}
adminsessions={'login' : False,'acid' : ""}

def home_function(request):
    return render(request,'home.html')

def monetory_function(request):
    return render(request,'monetory_donation.html')   
    
def donation_function(request) :
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    if request.method=='POST':
        medicine_name=request.POST['medicine_name']
        medicine_quantity=request.POST['medicine_quantity']
        donation_date=request.POST['donation_date']
        expiry_date=request.POST['expiry_date']
        DonationModel(status="pending",user_id=usersessions['userid'],medicine_name=medicine_name,medicine_quantity=medicine_quantity,donation_date=donation_date,expiry_date=expiry_date).save()
        return render(request, "medicine_donation.html")
    return render(request,"medicine_donation.html")

def request_function(request) :
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    if request.method=='POST':
        medicine_name=request.POST['medicine_name']
        medicine_quantity=request.POST['medicine_quantity']
        request_date=request.POST['request_date']
        DonationModel.objects(status="pending",user_id=usersessions['userid'],medicine_name=medicine_name,medicine_quantity=medicine_quantity,request_date=request_date).save()
        return render(request, "medicine_request.html")
    return render(request,"medicine_request.html")

def feedback_function(request) :
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    context ={}
    # create object of form
    form = FeedbackForm(request.POST or None, request.FILES or None)      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()  
    context['form']= form
    return render(request, "user_feedback.html", context)

def register(request):
    return render(request,"register.html")

def show(request):
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})    
    data=Entry.objects.all()
    return render(request,"show.html",{'data': data})

def enterotp(request):
    if request.method=='POST':
        otp=request.POST['otp'] 

def send(request):
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    if request.method=='POST':
        userid=request.POST['user_id']
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        adhaar=request.POST['adhaar']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

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

def edit(request):
    if usersessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    adhaar=request.GET['adhaar']
    name=address=email=phone=pass1="Not Available"
    for data in Entry.objects.filter(adhaar=adhaar):
        name=data.name
        address=data.address
        email=data.email
        phone=data.phone
        pass1=data.pass1
    return render(request,"edit.html",{'name':name,'address':address,'email':email,'phone':phone,'adhaar':adhaar,'pass1':pass1})

def RecordEdited(request):
    if  usersessions['login']==True:
        if request.method=='POST':
            name=request.POST['name']
            address=request.POST['address']
            email=request.POST['email']
            phone=request.POST['phone']
            adhaar=request.POST['adhaar']
            pass1=request.POST['pass1']
            Entry.objects.filter(adhaar = adhaar).update(name=name,address=address,email=email,phone=phone,adhaar=adhaar,pass1=pass1)
            return HttpResponseRedirect("show")
        else:
            return HttpResponse("<h1>f1</h1>") 
    else:
        return HttpResponse("<h2>404-Error page not found !</h2>")
   
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
            userinfo={'userid' : user.user_id,'name' : user.name,'email' : user.email,'phone' : user.phone,'address' : user.address}
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

    if MedicineStockModel.objects.filter(medicine_name=medicine_name).first() is not None :
        add=DonationModel.objects.filter(donate_id=donate_id).first().medicine_quantity
        curr=MedicineStockModel.objects.filter(medicine_name=medicine_name).first().medicine_quantity
        MedicineStockModel.objects.filter(medicine_name=medicine_name).update(medicine_quantity=curr+add)
    else :
        add=DonationModel.objects.filter(donate_id=donate_id).first().medicine_quantity
        MedicineStockModel(medicine_name=medicine_name,medicine_quantity=add).save()  
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
    return render(request,'Donationcheck.html',{'data':data})
    
def adminlogin(request):
    if request.method=='POST':
        acid=request.POST.get('acid')
        pass1=request.POST.get('pass1')

        member=Activemembers.objects.filter(acid=acid,pass1=pass1).first()

        if member is not None:
            adminsessions['login']=True
            adminsessions['acid']=acid
            data={'acid' : member.acid,'name' : member.name,'email' : member.email,'address' : member.address,'phone' : member.phone}
            return render(request,'AdminProfile.html',data)
        else :
            msg="Wrong Credentials"
            return render(request,'AdminLogin.html',{'msg' : msg})

    return render(request,'AdminLogin.html')

def requests(request):
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    data=RequestModel.objects.filter(status="pending")
    return render(request,'Requestcheck.html',{'data' : data})

def approverequest(request):
    if adminsessions['login']==False :
        return render(request,'login.html',{'msg' : "please login"})
    request_id=request.GET['request_id']
    medicine_name=DonationModel.objects.filter(request_id=request_id).first().medicine_name

    if MedicineStockModel.objects.filter(medicine_name=medicine_name).first() is not None :
        req=DonationModel.objects.filter(request_id=request_id).first().medicine_quantity
        curr=MedicineStockModel.objects.filter(medicine_name=medicine_name).first().medicine_quantity
        if req<curr :
            MedicineStockModel.objects.filter(medicine_name=medicine_name).update(medicine_quantity=curr-req)
        else:
            MedicineStockModel.objects.filter(medicine_name=medicine_name).update(medicine_quantity=0)
  
    return HttpResponseRedirect("requests")

def rejectrequest(request) :
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'login.html',{'msg' : msg})
    request_id=request.GET['request_id']
    DonationModel.objects.filter(request_id=request_id).update(status="Reject")
    return HttpResponseRedirect("requests")

def userlogout(request) :
    usersessions['userid']=""
    usersessions['login']=False
    return render(request,"home.html")

def adminlogout(request):
    adminsessions['acid']=""
    adminsessions['login']=False
    return render(request,"home.html")

def stocks(request):
    if adminsessions['login']==False :
        msg="Please Login"
        return render(request,'AdminLogin.html',{'msg' : msg})
    data=MedicineStockModel.objects.filter().all()
    return render(request,"stocks.html",{'data':data})    