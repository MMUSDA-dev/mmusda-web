from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.template import loader
from .models import Description


# Create your views here.
def index(request):
    # return HttpResponse('hello')
    return render(request, 'base/pages/index.html')


def about(request):
    latest_description = Description.objects.all().order_by('title')[:5]
    template = loader.get_template('base/pages/about.html')
    context = {
        'latest_description': latest_description,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    return render(request, 'base/pages/contact.html')
