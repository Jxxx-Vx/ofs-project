from django.shortcuts import render, redirect


#Create your views here
# from .models import Product,Customer
from .forms import CreateUserForm    # Django's built-in user form
from django.contrib import messages  # To add message whether login/registration sucesses or fails.
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# @login_required()
def index(request):
    """Placeholder index view"""
    return render(request, 'index.html')

def Meat_Seafood(request):
    """Placeholder Meat_Seafood view"""
    return render(request, 'Meat_and_Seafood.html')

def Fruits_Vegetables(request):
    """Placeholder Fruits_Vegetables view"""
    return render(request, 'Fruits_and_Vegetables.html')

def Pantry(request):
    """Placeholder Pantry view"""
    return render(request, 'Pantry.html')

def Beverages(request):
    """Placeholder Beverages view"""
    return render(request, 'Beverages.html')

def Dairy_Eggs(request):
    """Placeholder Dairy_Eggs view"""
    return render(request, 'Dairy_Eggs.html')

def Frozen_Foods(request):
    """Placeholder Frozen_Foods view"""
    return render(request, 'Frozen_Foods.html')


def registration_page(request):
    """ This function does 3 tasks:
        1. Display register.html path.
        2. Using a default form from forms.py, retrieve user's input from register.html page.
        3. Check if user's input is valid and if so, redirect to login page. """
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST) # Pass in user's information from registration.login
            if form.is_valid():
                form.save()  # Create new user in admin/
                user = form.cleaned_data.get('username')
                messages.success(request,'Account was created for ' + user)
                return redirect('login')         
        context = {'default_form':form}
        return render(request, 'accounts/register.html',context)



def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request,username=username,password=password)
            if user is not None: 
                login(request,user)
                return redirect('homepage')
            else:
                messages.info(request,'Username or password is incorrect!')
        context = {}
        return render(request, 'accounts/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')