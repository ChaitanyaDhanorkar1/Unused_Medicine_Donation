from distutils.command.upload import upload
from email.policy import default
from enum import auto
from django.db import models
import datetime

from django.forms import FileField
# Create your models here.

class DonationModel(models.Model):
    donate_id=models.AutoField(primary_key=True)
    status=models.CharField(default="pending",max_length=20)
    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.CharField(default='0',max_length=300)
    donation_date = models.DateField(default=datetime.datetime.now)
    expiry_date = models.DateField(default=datetime.datetime.now) 
    pickup_address=models.TextField(default="Not found")
    phone_no=models.CharField(default="Not found",max_length=20)
    def __str__(self):
        return self.user_id

# Model for Medicine Request Page
class RequestModel(models.Model):
    request_id=models.AutoField(primary_key=True)
    status=models.CharField(default="pending",max_length=20)
    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.CharField(max_length=50)
    request_date = models.DateField(default=datetime.datetime.now)
    purpose=models.TextField(null=True,blank=True)
    image=models.ImageField(null=True,blank=True)

    def __str__(self):
        return self.user_id

# Model for Medicine Stock
class MedicineStockModel(models.Model):
    
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    expiry_date = models.DateField(default=datetime.datetime.now)
    
    def __str__(self):
        return self.medicine_name
        
# Model for Customer Feedback Page
class FeedbackModel(models.Model):
    
    user_id = models.CharField(max_length=20, default=0)
    feedback = models.TextField()
    
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
    image=models.ImageField(null=True,blank=True)

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

    def __str__(self):
        return  self.name     
