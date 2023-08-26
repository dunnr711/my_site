
"""
URL configuration for my_site project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings
import os

# Define the URL patterns for the project
urlpatterns = [
    path('admin/', admin.site.urls),  # URL pattern for the admin site
    path("", include("blog.urls")),   # Include URLs from the "blog" app,
    path('tinymce/', include('tinymce.urls')),
]

# # Serve media files during development
if os.environ.get('ENVIRONMENT') == 'production':
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

    # Serve static files during development
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
