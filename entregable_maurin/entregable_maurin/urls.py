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
from anillos import views as anillos_views
from anteojos import views as anteojos_views
from clientes import views as clientes_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('anillos/', anillos_views.anillo_form, name='anillo_form'),
    path('anteojos/', anteojos_views.anteojo_form, name='anteojo_form'),
    path('clientes/', clientes_views.cliente_form, name='cliente_form'),
]
