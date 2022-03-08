from django import forms
from .models import DonationModel,RequestModel,FeedbackModel

class DonationForm(forms.ModelForm):
    class Meta:
        model = DonationModel
        fields = "__all__"  

class RequestForm(forms.ModelForm):
    class Meta:
        model = RequestModel
        fields = "__all__"  

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = "__all__"  