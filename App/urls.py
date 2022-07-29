
from django.contrib import admin
from django.urls import path
from App.views import (MainPageView, RegistroUsuario, PanelUsuario, 
PerfilUsuario, UsuarioUpdate, About, AnuncioDetailView, AnuncioCreateView, 
AnuncioUpdateView, AnuncioDeleteView, UsuarioLogin, PanelLogout)

urlpatterns = [
    path('', MainPageView.as_view(), name="index"),
    
    path('registro/', RegistroUsuario.as_view(), name="Registro"),
    path('usuario-success/', PanelUsuario.as_view(), name="perfil-ok"),
    path('usuario/<pk>', PerfilUsuario.as_view(), name="perfil-usuario"),
    path("usario/<pk>/edit", UsuarioUpdate.as_view(), name="usuario-update"),
    path('about/', About.as_view(), name="about"),
    
    path('anuncio/<pk>/', AnuncioDetailView.as_view(), name='anuncio-detalle'),
    path('anuncio/create', AnuncioCreateView.as_view(), name ="anuncio-create" ),
    path('anuncio/<pk>/update', AnuncioUpdateView.as_view(), name ="anuncio-update" ),
    path('anuncio/<pk>/delete', AnuncioDeleteView.as_view(), name ="anuncio-delete" ),
    
    path("login_Panel_u/", UsuarioLogin.as_view(), name="panel_usuario_avisos"),
    path("logout/", PanelLogout.as_view(), name="panel-logout"),
]