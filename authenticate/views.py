# from django.shortcuts import render
# from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login, get_user_model
from django.contrib.auth.backends import ModelBackend
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User
from dashboard.views import dashboard_home
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib import messages


# Create your views here.

def home(request):
    if request.user.is_authenticated:
        return dashboard_home(request)
    else:
        return render(request, 'authenticate/signin.html')


def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                messages.info(request, f'you are now logged in as {username}')
                return redirect('/admin/')
            else:
                messages.error(request, 'Please enter the correct username and password. Note that both fields are case-sensitive.')
        else:
            messages.error(request, 'Please enter the correct username and password. Note that both fields are case-sensitive.')
    form = AuthenticationForm()
    return render(
        request, 'authenticate/signin.html', {"forms": form}
    )


def signup(request):
    return render(request, 'authenticate/signup.html')


def logout_request(request):
    logout(request)
    return redirect(request.messages.info(request, 'You have logged out successfully!'), 'signout')


def signout(request):
    return render(request, 'authenticate/logout.html')
