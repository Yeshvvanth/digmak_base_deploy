from django.shortcuts import render, redirect
from .forms import CustomerSignupForm,AccountantSignupForm, CustomerForm, AccountantForm
from django.contrib.auth import authenticate, login , logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Accountant, Customer

# Create your views here.
def home(request):
    if request.user.is_authenticated and request.user.user_type==1:
        return redirect('customer_home')
    elif request.user.is_authenticated and request.user.user_type==2:
        return redirect('accountant_home')
    return render(request,'home.html')


def accountantSignup(request):
    form = AccountantSignupForm()
    if request.method == "POST":
        form = AccountantSignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('accountant_login')
    context = {'form':form}
    return render(request,'accountant/register.html',context)

def customerSignup(request):
    form = CustomerSignupForm()
    if request.method == "POST":
        form = CustomerSignupForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            return redirect('customer_login')
    context = {'form':form}
    return render(request,'customer/register.html',context)

def customerLogin(request):
    if request.method=="POST":
        customer_username = request.POST.get('username')
        customer_password = request.POST.get('password')
        user = authenticate(request,username=customer_username,password=customer_password)
        if user is not None:
            login(request,user)
            return redirect('customer_home')
        else:
            messages.info(request,"Incorrect UserName and Password")

    return render(request,'customer/login.html')

def accountantLogin(request):
    if request.method=="POST":
        accountant_username = request.POST.get('username')
        accountant_password = request.POST.get('password')
        user = authenticate(request,username=accountant_username,password=accountant_password)
        if user is not None:
            login(request,user)
            return redirect('accountant_home')
        else:
            messages.info(request,"Incorrect UserName and Password")

    return render(request,'accountant/login.html')

def logoutUser(request):
    logout(request)
    return redirect('home')

@login_required(login_url='accountant_login')
def accountantHome(request):
    if request.user.user_type==2:
        return render(request,'accountant/accountant_home.html')
    else:
        return redirect('home')

@login_required(login_url='customer_login')
def customerHome(request):
    if request.user.user_type==1:
        accountants = Accountant.objects.filter(hour_rate__isnull=False,user__username__isnull=False)
        context = {'accountants':accountants}
        return render(request,'customer/customer_home.html',context)
    else:
        return redirect('home')

@login_required(login_url='customer_login')
def customerProfile(request):
    if request.user.user_type==1:
        customer = request.user.customer
        form = CustomerForm(instance=customer)
        if request.method=="POST":
            form = CustomerForm(request.POST,request.FILES,instance=customer)
            if form.is_valid():
                form.save()
        context = {"form":form}
        return render(request,'customer/customer_profile.html',context)
    else:
        return redirect('home')

@login_required(login_url='accountant_login')
def accountantProfile(request):
    if request.user.user_type==2:
        accountant = request.user.accountant
        form = AccountantForm(instance=accountant)
        if request.method == "POST":
            form = AccountantForm(request.POST,request.FILES,instance=accountant)
            if form.is_valid():
                form.save()
        context = {"form":form}
        return render(request,'accountant/accountant_profile.html',context)
    else:
        return redirect('home')
