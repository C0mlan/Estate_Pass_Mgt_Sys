from django.shortcuts import render,redirect
from .models import Guest
from .forms import GuestForm
import random
from django.utils.crypto import get_random_string
from django.http import JsonResponse

def home(request):
    form = GuestForm()
    if request.method == 'POST':
        form =GuestForm(request.POST)
        if form.is_valid():
            instance= form.save(commit=False)
            instance.code= random.randint(10000,99999)
            instance.save()

    context={'form':form}
    return render(request,'home.html',context)

def validate(request):
    result =None
    if request.method =="POST":
        value= request.POST.get('code')
        result = Guest.objects.filter(code = value).first()
    context ={'result':result}
    return render(request,'validate.html',context)


