from dataclasses import dataclass
from distutils.command.upload import upload
from email.policy import default
from enum import auto
from django.db import models
from datetime import date

from django.forms import FileField
# Create your models here.

class DonationModel(models.Model):
    donate_id=models.AutoField(primary_key=True)
    status=models.CharField(default="pending",max_length=200)
    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default='0')
    donation_date = models.DateField(default=date.today())
    expiry_date = models.DateField(default=date.today()) 
    pickup_address=models.TextField(default="Not found")
    phone_no=models.CharField(default="Not found",max_length=20)
    def __str__(self):
        return self.user_id

# Model for Medicine Request Page
class RequestModel(models.Model):
    request_id=models.AutoField(primary_key=True)
    status=models.CharField(default="pending",max_length=200)
    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    request_date = models.DateField(default=date.today())
    purpose=models.TextField(null=True,blank=True)
    image=models.FileField(null=True,blank=True,upload_to='prescription')

    def __str__(self):
        return self.user_id

# Model for Medicine Stock
class MedicineStockModel(models.Model):
    
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    status=models.CharField(default="Usable",max_length=200)
    expiry_date = models.DateField(default=date.today())
    
    def __str__(self):
        return self.medicine_name
        
# Model for Customer Feedback Page
class FeedbackModel(models.Model):
    
    user_id = models.CharField(max_length=20, default=0,primary_key=True)
    feedback = models.TextField()
    rating=models.IntegerField(default=5)
    
    def __str__(self):
        return self.user_id


# model for registration
class Entry(models.Model):
    user_id = models.CharField(max_length=20, default="lr1")
    name=models.CharField(max_length=30,default="lr")
    address=models.CharField(max_length=400)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    adhaar=models.CharField(max_length=12,primary_key=True)
    pass1=models.CharField(max_length=30)
    image=models.FileField(null=True,blank=True,default='profile/profile.png',upload_to='profile')

    def __str__(self):
        return  self.name

class Activemembers(models.Model):
    acid = models.CharField(max_length=20, default="lr1")
    name=models.CharField(max_length=30,default="lr")
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    adhaar=models.CharField(max_length=12,primary_key=True)
    pass1=models.CharField(max_length=30)
    image=models.FileField(null=True,blank=True,default='profile/profile.png',upload_to='profile')

    def __str__(self):
        return  self.name   

  
