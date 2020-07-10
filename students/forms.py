from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from . import models

class UserForm(UserCreationForm):
    email=forms.EmailField(widget=forms.EmailInput(attrs={'class':'form-control'}))
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'*****'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'*****'}))
    class Meta:
        model=User
        fields={'username','email','password1','password2'}

class ProfileForm(forms.ModelForm):
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    contact=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    
    picture=forms.ImageField(widget=forms.ClearableFileInput(attrs={'class':'form-control'}))
    class Meta:
        model=models.Profile
        fields={'address','contact','fees_paid','picture'}

class LoginForm(AuthenticationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control'}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'*****'}))
    class Meta:
        model=User
        fields={'username','password'}
