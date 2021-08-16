"""church URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.pages, name='pages')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='pages')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url 
from django.contrib import admin
from django.urls import path
from base import views as base_views
from dashboard import views as dashboard_view
from news import views as news_view
from authenticate import views as authenticate_views
from search import views as search_view
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', base_views.index, name='index'),

    # path('search', include('search.urls'), name='search'),

    # base urls
    path('about/', base_views.about, name='about'),
    path('contact/', base_views.contact, name='contact'),

    # dashboard urls
    path('dashboard_home/', dashboard_view.dashboard_home, name='dashboard_home'),

    # authentication views
    # path('login/', auth_views.LoginView.as_view(template_name='authenticate/signin.html'), name='login'),
    # path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    path('login/', authenticate_views.login_request, name='login'),
    path('logout/', authenticate_views.logout_request, name='logout'),
    path('signout/', authenticate_views.signout, name='signout'),
    path('pages/', authenticate_views.home, name='pages'),
    path('signup/', authenticate_views.signup, name='signup'),

    # news views
    path('news/', news_view.news_home, name='news'),

    #search
    path('search/', search_view.search, name='search'),
]

handler404 = 'base.views.error_404'

handler500 = 'base.views.error_500'

handler403 = 'base.views.error_403'

if settings.DEBUG:
    urlpatterns = urlpatterns + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns = urlpatterns + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
