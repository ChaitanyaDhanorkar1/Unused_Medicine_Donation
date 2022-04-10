from django import forms
from .models import FeedbackModel

class FeedbackForm(forms.ModelForm):
    class Meta:
        model = FeedbackModel
        fields = "__all__"  