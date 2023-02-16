from django.contrib import admin

from .models import Coche, Categoria

class CocheAdmin(admin.ModelAdmin):
     readonly_fields=('created', 'updated')
     list_display=('marca', 'modelo', 'author')
     ordering = ('marca', 'modelo', 'kilometros', 'precio')
     search_fields = ('marca', 'modelo', 'author__username', 'categoria__nombre')
     date_hierarchy = ('created')
     
class CategoriaAdmin(admin.ModelAdmin):
     readonly_fields=('created', 'updated')
     list_display = ('marca', 'descripcion')

admin.site.register(Coche, CocheAdmin)
admin.site.register(Categoria, CategoriaAdmin)