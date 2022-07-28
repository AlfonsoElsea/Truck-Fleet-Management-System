
from django.shortcuts import render, redirect
from  django.contrib.auth import authenticate,login , logout
from  django.contrib.auth.forms import UserCreationForm

from django.contrib import messages
from .forms import CreateUserForm
from django.contrib.auth.models import User 


def login_user(request):
    if request.user.is_authenticated:
        return redirect('truckregister:index')
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username,password=password)

        if user is not None:
            login(request, user)
            return redirect('truckregister:index')
        else: 
            messages.info(request, ("Username OR Password incorrect.."))
            return render(request, 'authenticate/login.html',{})
    return render(request, 'authenticate/login.html',{})

def logoutUser(request):
    logout(request)
    return redirect('login')

def register_user(request):
    if request.user.is_authenticated:
        return redirect('truckregister:index')
    form = CreateUserForm()
    context = {}
    if request.method == 'POST':
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password1']

        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+user)
            return redirect('login')
        else:
            messages.success(request, "There was an error creating de user...")
    context = {"form": form}
       
    return render(request, 'authenticate/register.html', context)