"""
URL configuration for GeoGamesMedieval project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings  # ← Добавили импорт
from django.conf.urls.static import static  # ← Добавили импорт

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
]

# ← ЭТОТ БЛОК РАЗДАЁТ КАРТИНКИ В РЕЖИМЕ РАЗРАБОТКИ
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)