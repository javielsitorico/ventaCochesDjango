from django.shortcuts import render
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from .forms import CocheForm
from .models import Coche, Categoria

class CocheListView(ListView):
     model = Coche
     
class CocheDetailView(DetailView):
     model = Coche
     
class CocheCreateView(CreateView):
     model = Coche
     form_class = CocheForm
     success_url = reverse_lazy('listado')

class CocheUpdateView(UpdateView):
     model = Coche
     fields = ['marca', 'modelo', 'kilometros', 'descripcion', 'precio', 'imagen', 'categorias']
     template_name_suffix = '_update'
     success_url = reverse_lazy('listado')

class CocheDeleteView(DeleteView):
     model = Coche
     success_url = reverse_lazy('listado')