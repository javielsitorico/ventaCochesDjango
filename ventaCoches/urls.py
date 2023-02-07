from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('coches/', include('coches.urls')),
    path('admin/', admin.site.urls),
]
