# Generated by Django 4.0.5 on 2022-08-09 00:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_delete_usuariopersonalizado_alter_anuncio_autor'),
    ]

    operations = [
        migrations.AddField(
            model_name='anuncio',
            name='celular_aviso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='App.usuario'),
        ),
    ]