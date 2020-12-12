
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from contas import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('login/', views.login_user, name='login'),
    path('login/submit', views.submit_login, name='submit'),
    path('logout/', views.logout_user),
    path('', views.index)
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)