"""tinderClone URL Configuration
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('tinderMain.urls')),
    path('admin/', admin.site.urls),
]
