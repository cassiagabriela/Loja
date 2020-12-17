
from django.contrib import admin
from django.urls import path
from django.views.generic import TemplateView
from contas import views
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.ListaProdutosView.as_view(), name='index'),
    path('login/', views.LoginView.as_view(), name='login'),
    path('logout/', views.LogoutView.as_view(), name='logout'),
    path('registro/', views.RegistroView.as_view(), name='registro'),
    path('produtos/all/', views.ListaProdutosView.as_view(), name='produtos'),
    path('produtos/meus/', views.FilterMyProductsView.as_view(), name='meus'),
    path('produto/detalhe/<pk>/', views.DetalhesView.as_view(), name='detalhe'),
    path('produtos/promocao/', views.FilterPromocaoView.as_view(), name='promocao'),
    path('produtos/<str:categoria>/', views.FilterCategoriasView.as_view(), name='categoria'),
    path('cadastrar/', views.CriaProdutoView.as_view(), name='cadastro'),
    path('delete/<pk>/', views.DeleteProdutoView.as_view(), name='delete'),
    path('editar/<pk>', views.AtualizarProdutoView.as_view(), name='edite'),

]
urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)