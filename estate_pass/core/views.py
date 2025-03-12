from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Guest,Passer
from django.contrib.auth.models import User,auth
from django.contrib.auth.decorators import login_required
from .forms import GuestForm

import random
import string


def generate_code():
    """Generate a random 6-character alphanumeric code."""
    return ''.join(random.choices(string.digits, k=6))

@login_required(login_url='login')
def home(request):
    guest_1 = None
    code_1 = None
    
    if 'guest_id' in request.session:
        try:
            guest_1 = Guest.objects.get(id=request.session.pop('guest_id'))
            passer = Passer.objects.get(user=guest_1) 
            code_1 = passer.code
        except Guest.DoesNotExist:
            guest_1 = None
        except Passer.DoesNotExist:
            code_1 = None

    form = GuestForm(request.POST or None)
    if request.method == 'POST' and form.is_valid():
        guest = form.save(commit=False)
        guest.flat_no = request.user
        guest.save()

        
        passer = Passer.objects.create(user=guest, code=generate_code())

      
        request.session['guest_id'] = guest.id

        return redirect('home')

    context = {
        'form': form,
        'guest_1': guest_1,
        'code_1': code_1
    }
    return render(request, 'home.html',context)



@login_required(login_url='login')
def validate(request):
    guest = None
    error_message = None
    if request.method == "POST":
        value = request.POST.get('code')

        try:
            passer = Passer.objects.get(code=value) 
            guest = passer.user 
        except Passer.DoesNotExist:
            error_message = "Code is invalid."

    context = {
        "guest": guest,
        "error_message": error_message
    }
    return render(request,'validate.html', context)


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
    
#The login func.
def loginPage(request):
    if request.method == 'POST':
        username= request.POST['username']
        password= request.POST['password']
        
        user= auth.authenticate(username=username, password=password)
        
        if user is not None:
            auth.login(request, user)
            if user.is_superuser or user.is_staff: #Redirects superuser or staff to validation page
                return redirect('validate')
            return redirect("/")
        else:
            messages.info(request, "Invalid login details")
            return redirect('login')

    return render(request, 'login.html')
#The logout func.
def logOut(request):
    auth.logout(request)
    return redirect('login')


#Retrieves the username of users that are non-staff
@login_required(login_url='login')
def allFlat(request):
    flats = User.objects.filter(is_staff=False)
    context={'flats':flats}
    return render(request, 'flats.html', context)

#Retrieves a flat with the pk
@login_required(login_url='login')
def aFlat(request, pk):
    flat= User.objects.get(pk=pk)
    guests= Guest.objects.filter(flat_no=flat)
    context={'flat':flat,
             'guests':guests}
    return render(request, 'aflat.html', context)
