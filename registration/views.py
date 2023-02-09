from django.contrib.auth.forms import UserCreationForm
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

class RegistroView(CreateView):
     form_class = UserCreationForm
     success_url = reverse_lazy('login')
     template_name = 'registration/registro.html'
     
     def get_success_url(self) -> str:
          return reverse_lazy('login') + '?registrado'
     
     # Asi es como se generarian formularios en tiempo de ejecucion, pudiendo cmodificarlos como queramos
     # def get_form(self, form_class: None):
     #      form = super(RegistroView, self).get_form()
     #      form.fields['_username'].widget = forms.textInput(aatrs={'placeholder':'...', 'style':'background-color: red'})
     #      form.fields['_password1'].widget = forms.textInput(aatrs={'placeholder':'...', 'style':'background-color: red'})  
     #      form.fields['_password2'].widget = forms.textInput(aatrs={'placeholder':'...', 'style':'background-color: red'})  
     #      return form