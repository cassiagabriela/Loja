from django.db import models


class Produto(models.Model):

    titulo = models.CharField(max_length=100)
    descricao = models.TextField()
    referencia = models.CharField(max_length=5)
    preco = models.CharField(max_length=8)
    imagem = models.ImageField(null=True)

    def _str_ (self):
        return self.titulo

    class Meta:
        db_table = 'Produto'

