from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
User = get_user_model()
from .forms import CustomUserChangeForm, CustomUserCreationForm,LoginForm
from django.contrib.auth import authenticate, login ,logout
from django.contrib.auth.decorators import login_required
from . helpers import send_otp_to_phone

@login_required
def home(request):
    return render(request,'home.html')

def register(request):
    form = CustomUserCreationForm()
    if request.method == 'POST':
        email =request.POST['email']
        phone = request.POST['phone']
        password = request.POST['password']
        conformpassword = request.POST['conformpassword']
        if password == conformpassword:
            U = User.objects.create(email=email,phone=phone)
            U.set_password(password)
            U.save()
            send_otp_to_phone(phone,U)
            return render(request,'login.html')
        else:
            form = CustomUserCreationForm(request.POST)
            return render(request,'register.html',{'form':form})
        

    return render(request,'register.html',{'form':form})

def login_user(request):
    form = LoginForm()
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
        return redirect('/')
    return render(request,'login.html',{'form':form})

def logout_view(request):
    logout(request)
    return redirect('/')

def verifyotp(request):
    if request.method == 'POST':
        phone = request.POST['phone']
        otp = request.POST['otp']
        user_obj = User.objects.get(phone=phone)
        if user_obj.otp == otp:
            user_obj.is_phone_verified = True
            user_obj.save()
            return render(request,'succesfull.html')
        else:
            return render(request,'wrong.html')
    return render(request,'otp.html')