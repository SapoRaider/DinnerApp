from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
# Create your views here.


def index(request):
    return render(request, 'DinnerApp/index.html')


def profile(request):
    return render(request, 'DinnerApp/profile.html')

def login(request):
    data = {
        "Title":"Login",
        "css": "DinnerApp/css/login.css"
    }
    return render(request, 'registration/login.html',data)



def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data[username]
            messages.success(request, f'Usuario {username} creado')
    else:
        form = UserCreationForm()

    context = {'form' : form}


    return render(request, "registration/register.html", context)
