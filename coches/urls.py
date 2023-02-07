from django.urls import path
from . import views

urlpatterns = [
     path('', views.CocheListView.as_view(), name='listado'),
     path('coche/<int:pk>', views.CocheDetailView.as_view(), name='detalle'),
     path('anadir', views.CocheCreateView.as_view(), name='anadir'),
     path('modificar/<int:pk>', views.CocheUpdateView.as_view(), name='modificar'),
     path('borrar/<int:pk>', views.CocheDeleteView.as_view(), name='borrar'),    
]