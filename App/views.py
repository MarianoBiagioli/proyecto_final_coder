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
from django import forms
from .forms import *
from django.contrib import messages

# ver de borrar lo de abajo si no se usa
from django.db import models, transaction 
from ckeditor.fields import RichTextField
from django.contrib.auth import login, logout, authenticate
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

    #    if queryset:
    #        anuncios = Anuncio.objects.filter(
    #        Q(titulo__icontains = queryset) |
    #        Q(descripcion__icontains = queryset)
    #    ).distinct()
    #    return render(request, "index.html", {'anuncios': anuncios})


#class PanelLogin(SuccessMessageMixin, LoginView, CreateView):
    #template_name = 'App/log-in.html'
   # success_url = reverse_lazy("index")
    #success_message = "¡Bienvenido!"


class PanelLogout(LogoutView):
    template_name = 'App/panel_logout.html'

class PanelView(LoginRequiredMixin, ListView):
    
    queryset = Anuncio.objects.all()
    template_name = "App/anuncios.html"    
    context_object_name = "anuncios"


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
        context['anuncio'] = Anuncio.objects.order_by('date_updated').first()
        return context
    

#Desde acá vistas por tema Usuario/Autor anuncios

class RegistroUsuario(SuccessMessageMixin, CreateView):
    template_name = "sign-up.html"
    success_url = reverse_lazy("operacion-ok")
    form_class = UserCreationForm
    #success_message = "¡¡ Se creo tu perfil satisfactoriamente !!"
    
class PerfilUsuario(LoginRequiredMixin, UserPassesTestMixin, DetailView):

    model = Usuario
    template_name = "App/detalles-usuario.html"

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


class UsuarioLogin(LoginView):
    template_name = 'App/log-in.html'
    next_page = reverse_lazy("operacion-ok")




# Create your views here.
class Success(TemplateView):

    template_name = "App/operacion-ok.html"
    
   # def test_func(self):
   #     return self.request.user.id == int(self.kwargs['pk'])



class About( TemplateView):

    template_name = "App/about.html"


   

class PanelUsuario(LoginRequiredMixin, BaseView, ListView,):
    
    queryset = Anuncio.objects.all()
    template_name = "App/panel_usuario_avisos.html"
    context_object_name = "anuncios"
    
    def get_queryset(self):
        return Anuncio.objects.filter(autor=self.request.user)




    #def test_func(self):
      # return self.request.user.id == int(self.kwargs['pk'])


        
    
#filter(autor = )
   # filter(autor=int("pk")).values()
    #def test_func(self):
      #return self.request.user.id == int(self.kwargs['pk'])


#class PanelView(LoginRequiredMixin, BaseView, ListView):
    
   # queryset = Article.objects.all()
   # template_name = "news_portal/article_list.html"    
    #context_object_name = "articles"

    


#ACA HAY QUE METER ESTO

class PerfilUsuario(LoginRequiredMixin,UserPassesTestMixin, DetailView):

    model = Usuario
    template_name = "App/detalles-usuario.html"

    def test_func(self):
      return self.request.user.id == int(self.kwargs['pk'])


#ESTA VISTA EST AEN USO Y ES LA QUE LISTA LOS ANUNCIOS




      ###############
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.models import User
from App.forms import ProfileForm
from django.http import HttpResponseRedirect
from django.urls import reverse

from django.shortcuts import render, redirect
from .forms import FormularioContacto
from django.core.mail import send_mail, BadHeaderError
from django.http import HttpResponse


# PARA FORMULARIO DE CONTACTO

def homepage(request):
	return render(request, "main/home.html")

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




