from django import forms
from . import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class StudentRegister(forms.ModelForm):
    name=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'name'}))
    address=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address'}))
    contact=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control','placeholder':'contact'}))
    email=forms.CharField(widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}))
    class Meta:
        model=models.NewStudent
        fields={'name','address','contact','email','picture'}

class SignUpForm(UserCreationForm):
    username=forms.CharField(max_length=40)
    email=forms.EmailField(max_length=100)
    address=forms.CharField(max_length=200)
    contact=forms.IntegerField()


    class Meta:
        model=User
        fields=('username','email','address','contact','password1','password2',)
