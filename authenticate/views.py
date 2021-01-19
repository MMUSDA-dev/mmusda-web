from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, authenticate, login
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
                return redirect('dashboard_home')
            else:
                messages.error(request, 'invalid username or password')
        else:
            messages.error(request, 'invalid username or password')
    form = AuthenticationForm()
    return render(
        request, 'authenticate/signin.html', {"forms": form}
    )


def signup(request):
    return render(request, 'authenticate/signup.html')


def logout_request(request):
    logout(request)
    messages.info(request, 'logged out successfully!')
    return redirect('signout')


def signout(request):
    return render(request, 'authenticate/logout.html')
