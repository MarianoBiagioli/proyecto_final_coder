from django import forms
class ProfileForm(forms.Form):
    first_name = forms.CharField(label='First Name', max_length=50, required=False)
    last_name = forms.CharField(label='Last Name', max_length=50, required=False)

class FormularioContacto(forms.Form):
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=150)
    telefono = forms.CharField(max_length=50)
    mensaje = forms.CharField(widget = forms.Textarea, max_length = 2000)
    
