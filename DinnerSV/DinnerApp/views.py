from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .forms import *
from django.contrib import messages
# Create your views here.


def index(request):
    data ={
        "imgindex":"DinnerApp/img/img1.jpg"
    }
    return render(request, 'DinnerApp/index.html',data)


def profile(request):
    return render(request, 'DinnerApp/profile.html')

def loginuser(request):

    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password )
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            messages.success(request, ("Ups!, hubo un error iniciando sesion."))
            return redirect('home')

    data = {
        "Title":"Login",
        "css": "DinnerApp/css/login.css",
    }
    return render(request, 'registration/login.html',data)

def logoutuser(request):
    logout(request)
    messages.success(request,("has cerrado sesion!"))
    return redirect('home')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username,password=password)
            login(request, user)
            messages.success(request, f'Usuario {username} creado')
            return redirect("/")

    else:
        form = UserRegisterForm()

    data = {
        'form' : form
    }


    return render(request, "DinnerApp/register.html", data)


# def restaurantes(request):
