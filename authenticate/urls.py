from django.urls import path
from authenticate import views
from django.contrib import admin

urlpatterns = [
    path('', views.logout_request.as_View(next_page='/'), name='logout')
]