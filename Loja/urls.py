
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from contas import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('produtos/all/', views.lista, name='produtos'),
    path('produtos/promocao/', views.promocao, name='promocao'),
    path('produtos/<str:categoria>/', views.categorias, name='categoria'),
    path('produtos/detalhes/<id>/', views.detalhes, name='detalhes'),
    path('login/', views.login_user, name='login'),
    path('login/submit/', views.submit_login, name='submit'),
    path('logout/', views.logout_user),
    path('', views.lista, name='index')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)