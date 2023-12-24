from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, UserModel
from . import models    
class BuscarUsuarioForm(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
        
        
class CrearUsuarioForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField()
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir Contraseña", widget=forms.PasswordInput)
    fecha_nacimiento = forms.DateField()
    
    class Meta:
        model = UserModel
        fields = ["email","password1","password2","username","first_name","last_name","username"]
        
class UserEditionFormulario(UserChangeForm):
    email = forms.EmailField()
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)
    nombre = forms.CharField(label="Nombre")
    apellido = forms.CharField(label="Apellido")

    class Meta:
        model = UserModel
        fields = ["email", "password1", "password2", "nombre", "apellido",]

        
class UserAvatarFormulario(forms.ModelForm):

    class Meta:
        model = models.Avatar
        fields = ["imagen"]
        
        
        
class Comentarform(forms.ModelForm):
    
    class Meta:
        model = models.Comentario
        fields = ["autor","texto","post"]
        
        
class Editarcomentarioform(forms.ModelForm):
    
    class Meta:
        model = models.Comentario
        fields = ["texto","post"]
        
        