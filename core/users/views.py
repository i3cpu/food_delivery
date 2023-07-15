from django.shortcuts import render, redirect
from django.contrib import auth, messages
from users.forms import UserLoginForm, UserRegistartionForm, UserProfile
from users.models import User


# Create your views here.

def login(request):
    if request.method == 'POST':
        form = UserLoginForm(data = request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = auth.authenticate(username = username, password = password)
            if user:
                auth.login(request, user)
                return redirect('main_page')
            # else:
            #     form = UserLoginForm()
            #     return render(request, 'users/login.html', {'form':form, 'error':'error'})
    else:
        form = UserLoginForm()
    return render(request, 'users/login.html', {'form':form})

def registration(request):
    if request.method == 'POST':
        form = UserRegistartionForm(data = request.POST)
        if form.is_valid():
            form.save() 
            messages.success(request, 'Вы успешно зарегстрированы!')        
            return redirect('login')
    else:
        form = UserRegistartionForm()
    return render(request, 'users/registration.html', {'form':form})

def userprofile(requsest):
    if requsest.method == 'POST':
        form = UserProfile(instance = requsest.user, data = requsest.POST, files = requsest.FILES)
        if form.is_valid():
            form.save()
            return redirect('userprofile')
    else:
        # post = User.objects.filter(username = requsest.user)
        form = UserProfile(instance = requsest.user)
    return render(requsest, 'users/userprofile.html',{'form':form})

def logout(request):
    auth.logout(request)
    return redirect('main_page')