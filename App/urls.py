from django.contrib import admin
from django.urls import path, include
from App.views import (MainPageView, RegistroUsuario, PanelUsuario, 
PerfilUsuario, Success, UsuarioUpdate, About, AnuncioDetailView, AnuncioCreateView, 
AnuncioUpdateView, AnuncioDeleteView, UsuarioLogin, PanelLogout, contacto, profile_update, PanelUsuario)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', MainPageView, name="index"),
    path('registro/', RegistroUsuario.as_view(), name="Registro"),
    path('usuario-success/', Success.as_view(), name="operacion-ok"),
    path('usuario/<pk>', PerfilUsuario.as_view(), name="perfil"),
    path("usuario/<pk>/edit", UsuarioUpdate.as_view(), name="usuario-update"),
    path('about/', About.as_view(), name="about"),
    path('contacto/', contacto, name="contacto"),
    
    path('anuncio/<pk>/', AnuncioDetailView.as_view(), name='anuncio-detalle'), #FUNCIONANDO
    path('anuncio/create', AnuncioCreateView.as_view(), name ="anuncio-create" ), #FUNCIONANDO
    path('anuncio/<pk>/update', AnuncioUpdateView.as_view(), name ="anuncio-update" ),
    path('anuncio/<pk>/delete', AnuncioDeleteView.as_view(), name ="anuncio-delete" ),
    
    path("login/", UsuarioLogin.as_view(), name="login"),
    path("panel/<pk>", PanelUsuario.as_view(), name= "panel-usuario"),
    path("logout/", PanelLogout.as_view(), name="logout"),


    #path('anuncios/', anuncios_index, name='anuncios-index'),

    path('accounts/', include('django.contrib.auth.urls')),
    #path("panel_usuario/", PerfilUsuario.as_view(), name="panel-usuario"),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)