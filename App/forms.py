from django import forms
from App.models import User, Usuario

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('first_name', 'last_name', 'email')

class UsuarioForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ('celular', 'provincia', 'pais', 'descripcion_docente' , 'date_updated')
        

class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)
    celular = forms.IntegerField()

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    telefono = forms.CharField(max_length=50)
    mensaje = forms.CharField(widget = forms.Textarea, max_length = 2000)
    
