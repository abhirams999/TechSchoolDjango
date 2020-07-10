

# Create your views here.
from django.shortcuts import render,redirect,HttpResponse
from .models import NewStudent
from . import forms
from django.core.mail import send_mail as sm

# Create your views here.
def courses(request):
    return render(request,'admission/courses.html')

def registeration(request):
    if request.method=='POST':
        form=forms.StudentRegister(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect('home')

    else:
        form=forms.StudentRegister()
    return render(request,'admission/registeration.html',{'form':form})

def webdesign(request):
    return render(request,'admission/webdesign.html')

def appdevelopment(request):
    return render(request,'admission/appdevelopment.html')

def send_mail(request):
    res=sm(
    subject="trial message",
    message="hello world",
    from_email='abhirams999@gmail.com',
    recipient_list=['abhirams999@gmail.com'],
    fail_silently=False,
    )
    return HttpResponse("email sent to {res} members")
