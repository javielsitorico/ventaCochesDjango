from django import forms
from .models import Coche

class CocheForm(forms.ModelForm):
     class Meta:
          model = Coche
          fields = ['marca', 'modelo', 'kilometros', 'descripcion', 'precio', 'imagen', 'author', 'categorias']
          # Esto se usaría para modificar el elemento que queramos de estilo o propiedades
          # widgets = {
          #      'nombre': forms.TextInput(attrs={'style': 'background-color: red'}),
          #      'subnombre': forms.TextInput(attrs={'placeholder': 'Inserta un subnombre'})
          # }