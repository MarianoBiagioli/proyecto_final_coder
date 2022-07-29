from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.models import AbstractBaseUser
from django.utils import timezone

class Usuario(models.Model):
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    t_usuario = (("1", "Administrador"), ("2", "Docente"))
    tipo_de_usuario = models.CharField(max_length = 20, choices = t_usuario, default = "1")
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    celular = models.IntegerField()
    descripcion_docente = models.CharField(max_length=1000)
    provincia = models.CharField(max_length=20)
    pais = models.CharField(max_length=20) #AGREGAR LISTADO DE PAISES
    date_created = models.DateTimeField(default=timezone.now)
    date_updated = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.user.last_name, self.user.first_name}"


class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=180)
    autor = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    #descripcion_docente_a = models.CharField(max_length=180)
    #avatar_docente = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    imagen = models.ImageField(upload_to="articles", null=True, blank=True)
    #contacto_mail =  models.CharField(max_length=180) #models.ForeignKey(Usuario.email)
    #contacto_celular = models.IntegerField()
    descripcion_clase = models.CharField(max_length=800)
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