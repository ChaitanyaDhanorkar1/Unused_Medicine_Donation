from distutils.command.upload import upload
from enum import auto
from django.db import models
import datetime
# Create your models here.

class DonationModel(models.Model):
    donate_id=models.AutoField(primary_key=True)
    status=models.CharField(default="pending",max_length=20)
    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    donation_date = models.DateField(default=datetime.datetime.today)
    expiry_date = models.DateField(default=datetime.datetime.today) 
    def __str__(self):
        return self.user_id

# Model for Medicine Request Page
class RequestModel(models.Model):
    request_id=models.AutoField(primary_key=True)
    status=models.CharField(default="pending",max_length=20)
    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    request_date = models.DateField(default=datetime.datetime.today)
    def __str__(self):
        return self.user_id

# Model for Medicine Stock
class MedicineStockModel(models.Model):
    
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    expiry_date = models.DateField(default=datetime.datetime.today())
    
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
    address=models.CharField(max_length=30)
    email=models.CharField(max_length=30)
    phone=models.CharField(max_length=30)
    adhaar=models.CharField(max_length=12,primary_key=True)
    pass1=models.CharField(max_length=30)
    image=models.ImageField(upload_to="static",default="static/er_diagram.jpeg")

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
