
from django.contrib import admin
from django.urls import path
from App.views import ActualizacionUsuario, MainPageView, PerfilUsuario, SignUpView, About, RegistroUsuario, PanelUsuario, UsuarioLogin

urlpatterns = [
    path('', MainPageView.as_view(), name="Index"),
    path('login/', UsuarioLogin.as_view()),
    path('registro/', RegistroUsuario.as_view(), name="Resistro"),
    path('usuario-success/', PanelUsuario.as_view(), name="perfil-ok"),
    path('detalle-usuario/<pk>', PerfilUsuario.as_view(), name="perfil-usuario"),
    path('edicion-usuario/<pk>', ActualizacionUsuario.as_view(), name="actualizcion-usuario"),
    #path('about/', About, name=About),
]