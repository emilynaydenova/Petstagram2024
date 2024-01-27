from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from Petstagram2024 import settings

urlpatterns = [
    path("admin/", admin.site.urls),
    path('', include('common.urls')),
    path('accounts/', include('accounts.urls')),
    path('pets/', include('pets.urls')),
    path('photos/', include('photos.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
