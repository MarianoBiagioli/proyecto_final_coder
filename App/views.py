from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, View, ListView
from django.contrib.messages.views import SuccessMessageMixin
from App.models import Anuncio, Usuario

class RegistroUsuario(CreateView):
    model = Usuario
    template_name = "sign-up.html"
    form_class = UserCreationForm
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"
    success_url = reverse_lazy("PanelU")


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'sign-up.html'
  success_url = reverse_lazy('index')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

# Create your views here.

class BaseView(View):
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['headline'] = Anuncio.objects.filter(is_headline=True).order_by('date_updated').first()
        return context  

def About(request):
    return render(request, "App/about.html", {})


class MainPageView(BaseView, ListView):
    queryset = Anuncio.objects.all()
    context_object_name = "Anuncio"
    template_name = "App/index.html"

class PanelUsuario(BaseView, ListView):
    queryset = Anuncio.objects.all()
    context_object_name = "Anuncio"
    template_name = "App/index_log.html"