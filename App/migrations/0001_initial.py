# Generated by Django 4.0.5 on 2022-07-26 19:29

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.CharField(max_length=20)),
                ('tipo_de_usuario', models.CharField(choices=[('1', 'Administrador'), ('2', 'Docente')], default='1', max_length=20)),
                ('avatar', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('nombre_apellido', models.CharField(max_length=40)),
                ('email', models.EmailField(max_length=254)),
                ('celular', models.IntegerField()),
                ('descripcion_docente', ckeditor.fields.RichTextField()),
                ('provincia', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=20)),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
            ],
        ),
        migrations.CreateModel(
            name='Anuncio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('materia', models.CharField(max_length=180)),
                ('descripcion_docente_a', models.CharField(max_length=180)),
                ('avatar_docente', models.CharField(max_length=180)),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='articles')),
                ('contacto_mail', models.CharField(max_length=180)),
                ('comtacto_celular', models.CharField(max_length=180)),
                ('descripcion_clase', ckeditor.fields.RichTextField()),
                ('date_created', models.DateTimeField(auto_now_add=True)),
                ('date_updated', models.DateTimeField(auto_now=True)),
                ('date_published', models.DateTimeField()),
                ('autor', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='App.usuario')),
            ],
        ),
    ]
