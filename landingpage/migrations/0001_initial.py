# Generated by Django 5.1.1 on 2024-09-24 22:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='HomePageGalleryView',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('alt', models.CharField(max_length=200, verbose_name='Nome Alternativo')),
                ('cover', models.ImageField(blank=True, default='', upload_to='home/covers/%Y/%m/%d', verbose_name='Foto')),
            ],
        ),
        migrations.CreateModel(
            name='Services',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('description', models.TextField(max_length=200, verbose_name='Descrição')),
                ('bootstrap_icon', models.CharField(max_length=200, verbose_name='Bootstrap icon')),
            ],
        ),
        migrations.CreateModel(
            name='ClientContact',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200, verbose_name='Nome')),
                ('email', models.EmailField(max_length=254, verbose_name='E-mail')),
                ('phone', models.CharField(max_length=20, verbose_name='Telefone')),
                ('message', models.TextField(max_length=300, verbose_name='Mensagem')),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='service', to='landingpage.services', verbose_name='Serviço')),
            ],
        ),
    ]
