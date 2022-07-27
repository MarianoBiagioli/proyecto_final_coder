from django.contrib import admin
from App.models import Usuario, Anuncio

# Register your models here.

class UsuarioAdmin(admin.ModelAdmin):
    fields = [
        "user", "tipo_de_usuario", "nombre_apellido", "email", "avatar","celular","provincia","pais", 
        ]

admin.site.register(Usuario)
admin.site.register(Anuncio)

