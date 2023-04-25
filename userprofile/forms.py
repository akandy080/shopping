from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from . models import *

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    first_name = forms.CharField(max_length=50)
    last_name = forms.CharField(max_length=50)
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name','email', 'password1', 'password2')

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['first_name', 'last_name', 'pix', 'email', 'phone', 'address', 'dob', 'nationality', 'gender', 'state']

        GENDER = [
            ('Male', 'Male'),
            ('Female', 'Female'),
            ('Others', 'Others'),
        ]

        STATE = [
            ('Enugu', 'Enugu'),
            ('Delta', 'Delta'),
            ('Ekiti', 'Ekiti'),
            ('Ogun', 'Ogun'),
            ('Lagos', 'Lagos'),
            ('Abia', 'Abia'),
            ('Akwa-Ibom', 'Akwa-Ibom'),
            ('Imo', 'Imo'),
        ]
        
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'First Name'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Last Name'}),
            'pix': forms.FileInput(attrs={'class': 'form-control', 'placeholder': 'Pix'}),
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'Email'}),
            'phone': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Phone Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Address'}),
            'dob': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Date of Birth'}),
            'nationality': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nationality'}),
            'gender': forms.Select(attrs={'class': 'form-control', 'placeholder': 'Gender'}, choices=GENDER),
            'state': forms.Select(attrs={'class': 'form-control', 'placeholder': 'State'}, choices=STATE),


        }