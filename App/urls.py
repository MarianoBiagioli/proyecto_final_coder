
from django.contrib import admin
from django.urls import path
from App.views import MainPageView, SignUpView, About, RegistroUsuario, PanelUsuario

urlpatterns = [
    path('', MainPageView.as_view()),
    path('login/', SignUpView.as_view()),
    path('registro/', RegistroUsuario.as_view(), name="ResistroU"),
    path('panelusuario/', PanelUsuario.as_view, name="PanelU"),
    #path('about/', About, name=About),
]