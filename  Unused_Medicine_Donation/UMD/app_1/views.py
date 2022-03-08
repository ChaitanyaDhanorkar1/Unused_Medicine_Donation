from django.shortcuts import render,HttpResponse
from datetime import date, datetime
from django.contrib import messages
from .forms import DonationForm,RequestForm,FeedbackForm

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
