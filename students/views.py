from django.shortcuts import render,redirect,get_object_or_404
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.contrib.auth import login,logout
from students.models import Profile
from .forms import UserForm,ProfileForm,LoginForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def signup(request):
    if request.method=='POST':
        u_form=UserForm(request.POST)
        p_form=ProfileForm(request.POST,request.FILES)
        if u_form.is_valid() and p_form.is_valid():
            user=u_form.save()
            p_form=p_form.save(commit=False)
            p_form.user=user
            p_form.save()
            login(request,user)
            return redirect('students:login')
    else:
        u_form=UserForm()
        p_form=ProfileForm()
    return render(request,'students/signup.html',{'u_form':u_form,'p_form':p_form})
def login_view(request):
    if request.method=='POST':
        form=LoginForm(data=request.POST)
        if form.is_valid():
            user=form.get_user()
            login(request,user)
            if 'next' in request.POST:
                return redirect(request.POST.get('next'))
            else:
                return redirect('students:studentprofile')

    else:
        form=LoginForm()
    return render(request,'students/login.html',{'form':form})
def student_profile(request):
    details=User.objects.get(username=request.user)
    return render(request,'details.html',{'details':details})
def logout_view(request):
    if request.method=='POST':
        logout(request)
        return redirect('home')

@login_required(login_url='students:login')
def update(request,pk):
    user_details=get_object_or_404(User,pk=pk)
    profile_details=get_object_or_404(Profile,pk=pk)
    post_data=request.POST or None
    file_data=request.FILES or None
    u_form=UserForm(post_data,file_data,instance=user_details)
    p_form=ProfileForm(post_data,file_data,instance=profile_details)
    if u_form.is_valid() and p_form.is_valid():
        user=u_form.save()
        p_form=p_form.save(commit=False)
        p_form.user=user
        p_form.save()
        return redirect('studentlist')
    return render(request,'students/update.html',{'u_form':u_form,'p_form':p_form})
