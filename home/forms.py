
from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from . models import *

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['full_name', 'email', 'message']

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email']

STATE = [
    ('Lagos', 'Lagos'),
    ('Delta', 'Delta'),
    ('Enugu', 'Enugu'),
    ('Jigawa', 'Jigawa'),
]
class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'email', 'phone', 'address', 'state', 'pix']
        widgets = {
            'first_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'First Name'}),
            'last_name':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last Name'}),
            'email':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Email Address'}),
            'phone':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Phone Number'}),
            'address':forms.TextInput(attrs={'class':'form-control', 'placeholder':'Home Address'}),
            'state':forms.Select(attrs={'class':'form-control', 'placeholder':'State'}, choices=STATE),
            'pix':forms.FileInput(attrs={'class':'form-control'})
        }



