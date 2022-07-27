from django.shortcuts import render
from django.db import models
from django.contrib.auth.models import User
from ckeditor.fields import RichTextField
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import CreateView, TemplateView, View, ListView, UpdateView, DetailView
from django.contrib.messages.views import SuccessMessageMixin
from App.models import Anuncio, Usuario
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required


class RegistroUsuario(SuccessMessageMixin, CreateView):
    model = Usuario
    template_name = "sign-up.html"
    form_class = UserCreationForm
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"
    success_url = reverse_lazy("perfil-ok")

class UsuarioLogin(LoginView):
    template_name = 'App/log-in.html'
    next_page = reverse_lazy("Index")


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

    


#ACA HAY QUE METER ESTO

class PerfilUsuario(LoginRequiredMixin,UserPassesTestMixin, DetailView):

    model = Usuario
    template_name = "App/detalles-usuario.html"

    def test_func(self):
      return self.request.user.id == int(self.kwargs['pk'])

class ActualizacionUsuario(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = Usuario
    template_name = "App/edicion-usuario.html"
    fields = ["nombre_apellido", "email", "celular"]

    def get_success_url(self):
      return reverse_lazy("actualizacion-usuario", kwargs={"pk": self.request.user.id})

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])