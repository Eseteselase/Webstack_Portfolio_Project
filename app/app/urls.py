"""app URL Configuration
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]
