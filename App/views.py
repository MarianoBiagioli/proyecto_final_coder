from django.urls import reverse_lazy
from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.views.generic import CreateView, TemplateView, View, ListView, UpdateView, DetailView, DeleteView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from App.models import Anuncio, Usuario

# ver de borrar lo de abajo si no se usa
from django.db import models 
from ckeditor.fields import RichTextField
from django.contrib.auth import login, logout, authenticate


#Acá vistas por tema Anuncios

class BaseView(View):

     def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = Anuncio.objects.filter(titulo=True).order_by('date_updated').first()
        return context    

class PanelLogin(LoginView):
    template_name = 'App/log-in.html'
    next_page = reverse_lazy("panel_usuario_avisos")


class PanelLogout(LogoutView):
    template_name = 'App/panel_logout.html'

class PanelView(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Anuncio.objects.all()
    template_name = "App/anuncios.html"    
    context_object_name = "anuncios"

class AnuncioCreateView(LoginRequiredMixin, CreateView):
    model = Anuncio
    fields = ['titulo','materia' , 'autor', 'imagen', 'descripcion_clase', 'date_created', 'date_updated']
    template_name = "App/creacion-anuncio.html"
    success_url = reverse_lazy("panel_usuario_avisos")

class AnuncioUpdateView(LoginRequiredMixin, BaseView, UpdateView):
    model = Anuncio
    template_name = "App/anuncio_update.html"
    fields = ['titulo','materia' , 'autor', 'imagen', 'descripcion_clase', 'date_created', 'date_updated']
    success_url = reverse_lazy('panel_usuario_avisos')
    

class AnuncioDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Anuncio
    success_url = reverse_lazy('panel_usuario_avisos')
    

class AnuncioDetailView(DetailView):
    model = Anuncio
    template_name = "anuncio_detalle.html"
    context_object_name = "anuncio"
    
    #def get_context_data(self, **kwargs):
    #    context = super().get_context_data(**kwargs)
    #    context['portal'] = Portal.objects.order_by('date_updated').first()
    #    return context
    

#Desde acá vistas por tema Usuario/Autor anuncios

class RegistroUsuario(SuccessMessageMixin, CreateView):
    template_name = "sign-up.html"
    success_url = reverse_lazy("panel_usuario_avisos")
    form_class = UserCreationForm
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"

class PerfilUsuario(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Usuario
    template_name = "App/detalles_usuario.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk']) 

class UsuarioUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):

    model = User
    template_name = "App/edicion-usuario.html"
    fields = ["email", "first_name", "last_name"]

    def get_success_url(self):
        return reverse_lazy("user-detail", kwargs={"pk": self.request.user.id})
    
    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])


class UsuarioLogin(LoginView):
    template_name = 'App/log-in.html'
    next_page = reverse_lazy("panel_usuario_avisos")


# Create your views here.

class About(BaseView, TemplateView):

    template_name = "App/about.html"


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
