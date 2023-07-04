from django.shortcuts import render,redirect
from django.template import RequestContext
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm,UserUpdateForm,ProfileUpdateForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

# Create your views here.
def register(request):
    if request.method=='POST':
        form=UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username=form.cleaned_data.get('username')
            messages.success(request,f'Account created for {username}!')
            messages.info(request,'you can now login')
            return redirect('blog-login')

        else:
            form=UserRegisterForm(request.POST)
            return render(request,'register.html',{'form':form})
    else:
            form=UserRegisterForm()
            return render(request,'register.html',{'form':form})
        
def login(request):
    return render(request, 'login.html')
def logout(request):
    
    return render(request,'logout.html')
@login_required
def profile(request):
    if request.method=='POST':
        u_form=UserUpdateForm(request.POST,instance=request.user)
        p_form=ProfileUpdateForm(request.POST,request.FILES,instance=request.user.profile)
        if u_form.is_valid() and p_form.is_valid():
             u_form.save()
             p_form.save()
             messages.success(request,'Account has been updated!')
             return redirect('blog-profile')
    else:
         u_form=UserUpdateForm(instance=request.user)
         p_form=ProfileUpdateForm(instance=request.user.profile)
    return render(request,'profile.html',{'u_form':u_form,'p_form':p_form})

