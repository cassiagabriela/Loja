
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from contas import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('produtos/all/', views.ListaProdutosView.as_view(), name='produtos'),
    path('detalhe/<pk>/', views.DetalhesView.as_view(), name='detalhe'),
    path('produtos/promocao/', views.promocao, name='promocao'),
    path('produtos/<str:categoria>/', views.categorias, name='categoria'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.logout_user, name='logout'),
    path('login/registro', views.registro, name='registro'),
    path('cadastrar/', views.cadastro, name='cadastro'),
    path('login/submit', views.registrar),
    path('', views.lista, name='index')
]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)