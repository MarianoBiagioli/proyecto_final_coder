from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, View, ListView
from django.contrib.messages.views import SuccessMessageMixin
from App.models import Anuncio, Usuario

class RegistroUsuario(CreateView):
    model = User
    template_name = "sign-up.html"
    form_class = Usuario
    success_url = reverse_lazy()

class PanelLogin(LoginView):
    template_name = 'Appl/log-in.html'
    next_page = reverse_lazy("panel-page")


class SignUpView(SuccessMessageMixin, CreateView):
  template_name = 'sign-up.html'
  success_url = reverse_lazy('index')
  form_class = UserCreationForm
  success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

# Create your views here.

class BaseView(View):
     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['headline'] = Anuncio.objects.filter(is_headline=True).order_by('date_updated').first()
        return context  

class About(BaseView, TemplateView):
    template_name = "App/about.html"


class MainPageView(BaseView, ListView):
    queryset = Anuncio.objects.all()
    context_object_name = "articles"
    template_name = "App/index.html"