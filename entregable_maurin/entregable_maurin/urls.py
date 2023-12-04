"""
URL configuration for entregable_maurin project.

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
from anillos import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('anillos/', views.anillo_form, name= 'anillo_form'),
]

from anteojos import views
urlpatterns = [
    path('anteojos/', views.anteojo_form, name= 'anteojo_form')
]

from clientes import views
urlpatterns = [
    path('clientes/', views.cliente_form, name= 'cliente_form')
]