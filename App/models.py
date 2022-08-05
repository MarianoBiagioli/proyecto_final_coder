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
    autor = models.ForeignKey(
    User,
    models.SET_NULL,
    blank=True,
    null=True,
    )
    imagen = models.ImageField(upload_to="App\static", null=True, blank=True) #sacamos cuando podamos meter imagen usuario
    descripcion_clase = RichTextField()
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.titulo}"


#ESTO NO VA PERO DEJEMOSLO POR AHORA


class UsuarioPersonalizado(AbstractBaseUser):
    username = models.CharField('Nombre de Usuario', unique=True, max_length=100)
    email = models.EmailField('Correo Electronico', unique=True, max_length=254)
    nombres = models.CharField('Nombre/s', max_length=200, blank=True, null=True)
    apellidos = models.CharField('Apellido/s', max_length=200, blank=True, null=True)
    imagen = models.ImageField('Imagen de Perfil', upload_to='perfil/', height_field=None, width_field=None)
    usuario_activo = models.BooleanField(default=True)
    usuario_administrador = models.BooleanField(default=False)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'nombres', 'apellidos']

    def __str__(self):
        return f'{self.nombres},{self.apellidos}'

    def has_perm(self,perm,obj = None):
        return True

    def has_module_perms(self,app_label):
        return True

    @property
    def is_staff(self):
        return self.usuario_administrador