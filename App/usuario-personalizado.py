from django.db import models
from django.contrib.auth.models import AbstractBaseUser

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