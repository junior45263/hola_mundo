from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from .forms import RegistrationForm, LoginForm
from .models import UserProfile
from django.contrib.auth import logout

def user_logout(request):
    logout(request)
    return redirect('index')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
    else:
        form = RegistrationForm()

    return render(request, 'registration/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user:
                login(request, user)
                next_url = form.cleaned_data.get('next', '/myapp/home/')
                print(f"Next URL: {next_url}")
                return redirect(next_url)
    else:
        form = LoginForm()

    return render(request, 'registration/login.html', {'form': form})



def home(request):
    users = UserProfile.objects.all()
    return render(request, 'home.html', {'users': users})


def index(request):
    return render(request, 'line_book.html')









