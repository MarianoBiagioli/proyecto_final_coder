# Generated by Django 4.0.5 on 2022-08-06 07:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_alter_anuncio_autor'),
    ]

    operations = [
        migrations.DeleteModel(
            name='UsuarioPersonalizado',
        ),
    ]
