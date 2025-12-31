from django import forms
from .models import PasswordEntry

class PasswordEntryForm(forms.ModelForm):
    class Meta:
        model = PasswordEntry
        fields = ['organization', 'website', 'category', 'email', 'username', 'password']
        widgets = {
            'password': forms.PasswordInput(), 
        }