from django import forms
from django.db import models, transaction 
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.messages.views import SuccessMessageMixin
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.urls import reverse_lazy, reverse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import CreateView, TemplateView, View, ListView, UpdateView, DetailView, DeleteView
from django.views import generic
from App.models import Anuncio, Usuario
from .forms import *
from ckeditor.fields import RichTextField
from django.db.models import Q

def MainPageView(request):
    queryset = request.GET.get("buscar")    
    print(queryset)
    anuncios = Anuncio.objects.all()

    if queryset:
        anuncios = Anuncio.objects.filter(
            Q(materia__icontains = queryset) |
            Q(descripcion_clase__icontains = queryset)
        ).distinct()

    return render(request, "index.html", {'anuncios': anuncios})


class BaseView(View):

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['titulo'] = Anuncio.objects.filter(titulo=True).order_by('date_created').first()
        return context 

class UsuarioLogin(LoginView):
    template_name = 'App/log-in.html'
    next_page = reverse_lazy("operacion-ok")

   
class PanelLogout(LogoutView):
    template_name = 'App/panel_logout.html'


class AnuncioCreateView(LoginRequiredMixin, CreateView):
    model = Anuncio
    fields = ['titulo','materia', "autor", 'imagen', 'descripcion_clase', 'date_created', 'date_updated']
    widgets = {'autor': forms.TextInput(attrs={'type': 'hidden'})}
    template_name = "App/anuncio_creacion.html"
    success_url = reverse_lazy("operacion-ok")
    def get_initial(self):
        return {'autor': self.request.user}

class AnuncioUpdateView(LoginRequiredMixin, UpdateView):
    model = Anuncio
    template_name = "App/anuncio_update.html"
    fields = ['titulo','materia' , 'autor', 'imagen', 'descripcion_clase', 'date_created', 'date_updated']
    success_url = reverse_lazy('operacion-ok')
    

class AnuncioDeleteView(LoginRequiredMixin, BaseView, DeleteView):
    model = Anuncio
    template_name = "App/confirm-delete.html"
    success_url = reverse_lazy('operacion-ok')
    

class AnuncioDetailView(DetailView):
    model = Anuncio
    template_name = "App/anuncio_detalle.html"
    context_object_name = "anuncio"
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['anuncio'] = Anuncio.objects.order_by('date_updated').first()
        #context['titulo'] = Anuncio.objects.filter(titulo=True).order_by('date_updated').first()
        return context
    

#Desde acá vistas por tema Usuario/Autor anuncios

class RegistroUsuario(SuccessMessageMixin, CreateView):
    template_name = "sign-up.html"
    success_url = reverse_lazy("login")
    form_class = UserCreationForm
    success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"    



class UserProfile(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Usuario
    template_name = "detalles-usuario.html"

    def test_func(self):
        return self.request.user.id == int(self.kwargs['pk'])

@login_required
@transaction.atomic
def profile_update(request, pk):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = UsuarioForm(request.POST, instance=request.user.usuario)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, ('Your profile was successfully updated!'))
            return redirect('operacion-ok')
        else:
            messages.error(request, _('Please correct the error below.'))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = UsuarioForm(instance=request.user.usuario)
    return render(request, 'App/edicion-usuario.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


# Create your views here.
class Success(TemplateView):

    template_name = "App/operacion-ok.html"



class About( TemplateView):

    template_name = "App/about.html"


class PanelUsuario(LoginRequiredMixin, BaseView, ListView):
    
    queryset = Anuncio.objects.all()
    template_name = "App/panel_usuario_avisos.html"
    context_object_name = "anuncios"
    
    def get_queryset(self):
        return Anuncio.objects.filter(autor=self.request.user)


# PARA FORMULARIO DE CONTACTO

def contacto(request):
	if request.method == 'POST':
		form = FormularioContacto(request.POST)
		if form.is_valid():
			subject = "Contacto" 
			body = {
			'nombre': form.cleaned_data['nombre'], 
			'apellido': form.cleaned_data['apellido'], 
			'email': form.cleaned_data['email'], 
			'mensaje':form.cleaned_data['mensaje'], 
			}
			message = "\n".join(body.values())

			try:
				send_mail(subject, message, 'admin@example.com', ['admin@example.com']) 
			except BadHeaderError:
				return HttpResponse('Error, vuelva a intentarlo.')
			return redirect ("operacion-ok")
      
	form = FormularioContacto()
	return render(request, "App/contacto.html", {'form':form})
