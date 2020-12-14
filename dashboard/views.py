from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth.models import User


# Create your views here.
@login_required
def dashboard_home(request):
    return render(request, 'dashboard/home.html')