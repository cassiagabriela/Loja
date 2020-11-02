
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from contas import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login, name='submit'),
    path('logout/', views.logout_user),
    path('', views.index)
]

