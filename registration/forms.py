from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

# Para añadir el campo mail al formulario de registro de usuario, creamos una clase
# que hereda de UserCreationForm

class UsuarioCustomCreateForm(UserCreationForm):
     email = forms.EmailField(required=True, help_text='Obligatorio. Máx 254 caracteres y un email válido')
     
     class Meta:
          model = User
          fields = ('username', 'email', 'password1', 'password2')
          
     def clean_email(self):
          email = self.cleaned_data.get('email')
          
          if User.objects.filter(email=email).exists():
               # raise es un una especie de return pero con error
               raise forms.ValidationError('El correo ya está registrado')
          
          return email