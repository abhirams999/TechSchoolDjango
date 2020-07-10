from django.shortcuts import render,redirect,get_object_or_404
from students.models import Profile
from django.contrib.auth.models import User
from django.contrib.auth import login,logout
from admission import forms
from django.core.mail import send_mail as sm

from django.contrib.auth.decorators import login_required
def home(request):
    if request.method=='POST':
        form=forms.StudentRegister(request.POST,request.FILES)
        if form.is_valid():
            instance=form.save(commit=False)
            instance.save()
            return redirect('home')

    else:
        form=forms.StudentRegister()
    return render(request,'home.html',{'form':form})

def student_list(request):
    list=Profile.objects.all()
    return render(request,'list.html',{'list':list})

@login_required(login_url='students:login')
def student_details(request,name):
    details=User.objects.get(username=name)
    return render(request,'details.html',{'details':details})

def about(request):
    return render(request, 'about.html')

def event(request):
    return render(request, 'events.html')

def gallery(request):
    return render(request, 'gallery.html')

def contact(request):
    if request.method=='POST':
        Name=request.POST['Name']
        Email=request.POST['Email']
        Subject=request.POST['Subject']
        Message=request.POST['Message']
        sm(
        Name+":  "+Subject,
        Message,
        Email,
        ['abhirams999@gmail.com'],
        fail_silently=False,
        )
        return render(request, 'contact.html',{'Name':Name})
    else:
        return render(request, 'contact.html')

def delete(request,name):
    student=User.objects.get(username=name)
    if request.method=='POST':
        if 'yes' in request.POST:
            student.delete()

            return redirect('studentlist')
        return redirect('students:studentprofile')
    return render(request,'delete.html',{'student':student})
