from django.contrib import admin
from .models import Produto
# Register your models here.

@admin.register(Produto)
class ProdutosAdmin(admin.ModelAdmin):
    list_display = ['titulo', 'referencia', 'preco']