from django import forms
from .models import Media

class MediaForm(forms.ModelForm):
    files = forms.FileField()  
    name = forms.CharField(max_length=100)  
    class Meta:
        model = Media
        fields = ['name', 'media']