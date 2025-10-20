from django import forms
from .models import PYQ

class PYQUploadForm(forms.ModelForm):
    class Meta:
        model = PYQ
        fields = ['title', 'subject', 'year', 'semester', 'file']