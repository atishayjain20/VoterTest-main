from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from .forms import UserRegisterForm
from .models import Voter
# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Account created for {username} !')
            return redirect('home')
    else:
        form = UserRegisterForm()

    return render(request, 'register.html', {'form': form})


def home(request):
    return render(request, 'home.html')
def login(request):
    if request.method=="POST":
        aadhar=request.POST['Aadhar']
        aadhar=int(aadhar)
        if Voter.objects.filter(aadhar=aadhar).exists():
            v1=Voter.objects.filter(aadhar=aadhar).first()
            print(v1.contact)
            return redirect("otp")
        else:
            return redirect("home")
    return render(request,'login.html')

def otp(request):
    otp="1234"
    if request.method == "POST":
        o1=request.POST['otp']
        if o1==otp:
            return render(request,"home.html")
    return render(request,"otp.html")