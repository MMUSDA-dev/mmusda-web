from django.shortcuts import render
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator
from django.db.models import F

# Create your views here

def search(request):
    search= request
    querystring = ''
    if 'q' in request.GET:
        querystring = request.GET.get('q').strip()


    return render(request, 'search/search.html')