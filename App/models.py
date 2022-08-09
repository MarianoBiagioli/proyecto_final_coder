from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone
from django.shortcuts import render
from django.db.models.signals import post_save
from django.dispatch import receiver

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    celular = models.IntegerField(null=True, blank=True)
    descripcion_docente = RichTextField()
    provincia = models.CharField(max_length=20)
    pais = models.CharField(max_length=20) 
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.last_name}, {self.user.first_name}"
    
    def avatar_url(self):
        if self.avatar and hasattr(self.avatar, 'url'):
            return self.avatar.url

@receiver(post_save, sender=User)
def create_user_usuario(sender, instance, created, **kwargs):
    if created:
        Usuario.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_usuario(sender, instance, **kwargs):
    instance.usuario.save()

class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=180)
    autor = models.ForeignKey(User, models.SET_NULL, blank=True, null=True)
    imagen = models.ImageField(upload_to="App\static", null=True, blank=True) 
    descripcion_clase = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titulo}"


