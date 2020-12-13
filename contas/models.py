from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager



class Produto(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    referencia = models.CharField(max_length=5)
    preco = models.CharField(max_length=15)
    imagem = models.ImageField(null=True, upload_to='images')
    quantidade = models.IntegerField(null=True)
    promocao = models.BooleanField(null=True)
    precopromocao = models.CharField(max_length=15, null=True)
    categoria = models.CharField(max_length=50, null=True)


    def _str_ (self):
        return self.id

    class Meta:
        db_table = 'Produto'

