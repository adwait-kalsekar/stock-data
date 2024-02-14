from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import CustomUserCreationForm

# Create your views here.

def user_login(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == 'POST':
        username = request.POST["username"]
        password = request.POST["password"]

        try:
            user = User.objects.get(username=username)
        except:
            messages.error(request, "Incorrect credentials")
            return redirect("login")

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "Incorrect credentials")
            return redirect("login")

    return render(request, 'account/login.html')

@login_required(login_url="login")
def user_logout(request):
    logout(request)
    messages.error(request, "User was logged out")
    return redirect("login")

def user_register(request):
    page = "register"
    form = CustomUserCreationForm()

    if request.user.is_authenticated:
        return redirect("home")
    
    if request.method == "POST":
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.username = user.username.lower()
            user.save()

            messages.success(request, "User Created Successfully!")

            login(request, user)
            return redirect("home")
        else:
            messages.error(request, "An error occurred during registration")
    
    context = { "page": page, "form": form }
    return render(request, "account/register.html", context)
