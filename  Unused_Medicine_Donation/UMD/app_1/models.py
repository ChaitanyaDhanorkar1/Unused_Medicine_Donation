from django.db import models
import datetime
# Create your models here.

# Model for Medicine Donation Page
class DonationModel(models.Model):

    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    donation_date = models.DateField(default=datetime.datetime.today())
    expiry_date = models.DateField(default=datetime.datetime.today())
    
    def __str__(self):
        return self.user_id

# Model for Medicine Request Page
class RequestModel(models.Model):

    user_id = models.CharField(max_length=20, default=0)
    medicine_name = models.CharField(max_length=100, default="Medicine")
    medicine_quantity = models.IntegerField(default=0)
    request_date = models.DateField(default=datetime.datetime.today())
    
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
