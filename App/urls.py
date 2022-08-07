from django.contrib import admin
from django.urls import path, include
from App.views import (MainPageView, RegistroUsuario, PanelUsuario, UserProfile, Success, About, AnuncioDetailView, AnuncioCreateView, 
AnuncioUpdateView, AnuncioDeleteView, UsuarioLogin, PanelLogout, contacto, profile_update, PanelUsuario)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPageView, name="index"), #Pagina de inicio
    path('registro/', RegistroUsuario.as_view(), name="Registro"), #crear usuarios
    path("login/", UsuarioLogin.as_view(), name="login"),
    path('usuario-success/', Success.as_view(), name="operacion-ok"),
    path('usuario/<pk>', PanelUsuario.as_view(), name="perfil"), #panel de usuario donde se ven los avisos
    path("usuario/<pk>/ver/", UserProfile.as_view(), name="usuario-detalle"),
    path("usuario/<pk>/edit", profile_update, name="usuario-update"), #modificar usuario
    path('about/', About.as_view(), name="about"), #about
    path('contacto/', contacto, name="contacto"), #contacto
    
    path('anuncio/<pk>/', AnuncioDetailView.as_view(), name='anuncio-detalle'), #ver el detalle de los anuncios
    path('anuncio/create', AnuncioCreateView.as_view(), name ="anuncio-create" ), #Crear anuncio
    path('anuncio/<pk>/update', AnuncioUpdateView.as_view(), name ="anuncio-update" ), #modifica anuncio
    path('anuncio/<pk>/delete', AnuncioDeleteView.as_view(), name ="anuncio-delete" ), #elimina avisos
    
    
    path("logout/", PanelLogout.as_view(), name="logout"),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)