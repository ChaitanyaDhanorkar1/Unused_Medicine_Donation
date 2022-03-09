from django.contrib import admin
from .models import DonationModel,RequestModel,MedicineStockModel,FeedbackModel,Entry
# Register your models here.
admin.site.register(DonationModel)
admin.site.register(RequestModel)
admin.site.register(MedicineStockModel)
admin.site.register(FeedbackModel)
admin.site.register(Entry)

