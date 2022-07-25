from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField



class Usuario(models.Model):
    user = models.CharField(max_length=20)
    t_usuario = (("1", "Administrador"), ("2", "Docente"))
    tipo_de_usuario = models.CharField(max_length = 20, choices = t_usuario, default = "1")
    avatar = models.ImageField(upload_to="avatars", null=True, blank=True)
    nombre_apellido = models.CharField()
    email = models.EmailField()
    celular = models.IntegerField()
    descripcion_docente = RichTextField()
    provincia = models.CharField(max_length=20)
    pais = models.CharField(max_length=20) #AGREGAR LISTADO DE PAISES
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.Usuario.user}"


class Anuncio(models.Model):
    titulo = models.CharField(max_length=100)
    materia = models.CharField(max_length=180)
    autor = models.ForeignKey(Usuario, on_delete=models.DO_NOTHING)
    descripcion_docente_a = models.ForeignKey(Usuario.descripcion_docente)
    avatar_docente = models.ForeignKey(Usuario.avatar)
    imagen = models.ImageField(upload_to="articles", null=True, blank=True)
    contacto_mail = models.ForeignKey(Usuario.email)
    comtacto_celular = models.ForeignKey(Usuario.celular)
    descripcion_clase = RichTextField()
    date_created = models.DateTimeField(auto_now_add=True)
    date_updated = models.DateTimeField(auto_now=True)
    date_published = models.DateTimeField()
