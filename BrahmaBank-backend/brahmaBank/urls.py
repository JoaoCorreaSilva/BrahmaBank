
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

from core.urls import router

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', include(router.urls)),

    # URLS DO DJOSER
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt'))

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
