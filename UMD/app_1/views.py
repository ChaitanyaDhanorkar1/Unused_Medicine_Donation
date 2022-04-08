from django.shortcuts import render,HttpResponse
from sqlalchemy import false
from .forms import DonationForm,RequestForm,FeedbackForm
from django.http import HttpResponse,HttpResponseRedirect
from app_1.models import Entry
import random
from twilio.rest import Client


def home_function(request):
    return render(request,'home.html')

def monetory_function(request):
    return render(request,'monetory_donation.html')   
    
def donation_function(request) :
    context ={}
    # create object of form
    form = DonationForm(request.POST or None, request.FILES or None)      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()  
    context['form']= form
    return render(request, "medicine_donation.html", context)

def request_function(request) :
    context ={}
    # create object of form
    form = RequestForm(request.POST or None, request.FILES or None)      
    # check if form data is valid
    if form.is_valid():
        # save the form data to model
        form.save()  
    context['form']= form
    return render(request, "medicine_request.html", context)

def feedback_function(request) :
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
    data=Entry.objects.all()
    return render(request,"show.html",{'data': data})

def enterotp(request):
    if request.method=='POST':
        otp=request.POST['otp'] 

def send(request):
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
    msg = client.messages.create(
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
            request.session['name']=user.name
            request.session['login']=True

            userinfo={'userid' : user.user_id,'name' : user.name,'email' : user.email,'phone' : user.phone,'address' : user.address}
            return render(request, 'profile.html',userinfo)
        else:
            # No backend authenticated the credentials
            msg="Wrong Credentials"
            return render(request, 'login.html',{'msg':msg})
    return render(request, 'login.html')
