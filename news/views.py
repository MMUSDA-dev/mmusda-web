from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import News
from django.template import loader

# Create your views here

def news_home(request):
    latest_news = News.objects.all().order_by('pub_date')[:5]
    template = loader.get_template('news/home.html')
    context = {
        'latest_news': latest_news,
    }
    return HttpResponse(template.render(context, request)) 
