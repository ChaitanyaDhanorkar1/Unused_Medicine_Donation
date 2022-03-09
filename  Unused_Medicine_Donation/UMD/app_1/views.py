from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from django.contrib import messages
from .forms import DonationForm,RequestForm,FeedbackForm
from django.http import HttpResponse,HttpResponseRedirect
from app_1.models import Entry
# Create your views here.

def home_function(request):
    return render(request,'home.html')
    
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

def send(request):
    if request.method=='POST':
        name=request.POST['name']
        address=request.POST['address']
        email=request.POST['email']
        phone=request.POST['phone']
        adhaar=request.POST['adhaar']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']
        if pass1==pass2 :
            Entry(name=name,address=address,email=email,phone=phone,adhaar=adhaar,pass1=pass1).save()
            msg="Data Stored Successfully!!"
            return render(request,"register.html",{'msg':msg})
        else:
            msg="Enter the same password "
            return render(request,"register.html",{'msg':msg})
    else:
         return HttpResponse("<h2>404-Error page not found !</h2>")

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
        adhaar = request.POST.get('adhaar')
        pass1 = request.POST.get('pass1')

        # check if user has entered correct credentials
        # user = authenticate(adhaar=adhaar, pass1=pass1)
        user=Entry.objects.filter(adhaar=adhaar,pass1=pass1).first()

        if user is not None:
            # A backend authenticated the credentials
            # login(request, user)
            msg="LoginSucess"
            return render(request, 'home.html',{'msg':msg})
        else:
            # No backend authenticated the credentials
            msg="Wrong Credentials"
            return render(request, 'login.html',{'msg':msg})
    return render(request, 'login.html')
