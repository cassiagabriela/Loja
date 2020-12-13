# Generated by Django 3.1.4 on 2020-12-13 16:10

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('contas', '0005_produto_usuario'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=50)),
            ],
            options={
                'db_table': 'User',
            },
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.RemoveField(
            model_name='produto',
            name='usuario',
        ),
    ]