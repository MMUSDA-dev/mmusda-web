from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, Http404
from django.template import loader
from .models import Description, IndexDescription


# Create your views here.
def error_404(request, exception):
    return render(request, '404.html')

def error_403(request, exception):
    return render(request, '403.html')

def error_500(request, exception):
    return render(request, '500.html')


def index(request):
    # return HttpResponse('hello')
    latest_index_view = IndexDescription.objects.all().order_by('title')
    template = loader.get_template( 'base/pages/index.html')
    context = {
        'latest_index_view' : latest_index_view
    }
    return HttpResponse(template.render(context, request))



def about(request):
    latest_description = Description.objects.all().order_by('title')[:5]
    template = loader.get_template('base/pages/about.html')
    context = {
        'latest_description': latest_description,
    }
    return HttpResponse(template.render(context, request))


def contact(request):
    return render(request, 'base/pages/contact.html')



