from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager
from django.contrib.auth.models import User

class Produto(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    referencia = models.CharField(max_length=5,)
    preco = models.DecimalField(max_digits=8,decimal_places=2)
    imagem = models.ImageField(null=True, upload_to='images')
    quantidade = models.IntegerField(null=True)
    promocao = models.BooleanField(null=True, default=False)
    precopromocao = models.DecimalField(max_digits=8,decimal_places=2, null=True, blank=True)
    categoria = models.CharField(max_length=50, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def _str_ (self):
        return self.id

    class Meta:
        db_table = 'Produto'

