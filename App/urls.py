
from django.contrib import admin
from django.urls import path
from App.views import RegistroUsuario, SignUpView

urlpatterns = [
    path('registro/', SignUpView.as_view())
]