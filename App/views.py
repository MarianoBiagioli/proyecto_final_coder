from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views.generic import CreateView

class RegistroUsuario(CreateView):
    model = User
    template_name = "sign-up.html"
    form_class = UserCreationForm
    success_url = reverse_lazy()

# Create your views here.
