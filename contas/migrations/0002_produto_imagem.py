# Generated by Django 3.1.4 on 2020-12-12 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='produto',
            name='imagem',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
