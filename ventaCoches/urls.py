from django.contrib import admin
from django.urls import path, include
from django.conf import settings

urlpatterns = [
    path('coches/', include('coches.urls')),
    path('cuentas/', include('django.contrib.auth.urls')),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)