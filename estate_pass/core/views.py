from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Guest
from django.contrib.auth.models import User,auth
from .forms import GuestForm
import random


def home(request):
    form = GuestForm()
    if request.method == 'POST':
        form =GuestForm(request.POST, )
        if form.is_valid():
            instance= form.save(commit=False)
            instance.flat_no = request.user 
            instance.code= random.randint(10000,99999)
            instance.save()

    context={'form':form}
    return render(request,'home.html',context)

def validate(request):
    result =None
    if request.method =="POST":
        value= request.POST.get('code')
        result = Guest.objects.filter(code = value).first()
    return render(request,'validate.html')


def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
    
        if password1 == password2:
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Username taken')
                return redirect('signup')
            else:
                try:
                    user = User.objects.create_user(username=username, password=password1)
                    user.save()
                except ValueError:
                    messages.info(request, f"Flat number is required")
                    return redirect('signup')
        else:
            messages.info(request, 'Password do not match')
            return redirect('signup') 
    return render(request, 'register.html')
    

def loginPage(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        
        user= auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            if user.is_superuser or user.is_staff:
                return redirect('validate')
            return redirect("/")
        else:
            messages.info(request, "Invalid login details")
            return redirect('login')

    return render(request, 'login.html')

def logOut(request):
    auth.logout(request)
    return redirect('login')

def allFlat(request):
    flats = User.objects.filter(is_staff=False)
    context={'flats':flats}
    return render(request, 'flats.html', context)
