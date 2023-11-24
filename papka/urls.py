"""
URL configuration for papka project.

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
from django.urls import path
from machines.views import index , indexe

urlpatterns = [
    path('admin/', admin.site.urls),
    path('machines/', index),           #http://127.0.0.1:8000/machines/
    path('', indexe) # так как в кавычках ничего не указано, то это будет показывать сайт при его открытии.
]
