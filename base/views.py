from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    return render(request, 'home/index.html')


def about(request):
    return render(request, 'home/about.html')


def contact(request):
    return render(request, 'home/contact.html')