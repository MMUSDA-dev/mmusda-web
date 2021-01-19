from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from . import models


# Create your views here.
def index(request):
    # return HttpResponse('hello')
    return render(request, 'base/pages/index.html')


def about(request):
    return render(request, 'base/pages/about.html')


def contact(request):
    return render(request, 'base/pages/contact.html')
