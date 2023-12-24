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
from anillos.views import AnilloListView, AnilloUpdateView, AnilloDeleteView, AnilloDetailView
from anteojos.views import AnteojoListView, AnteojoUpdateView, AnteojoDeleteView, AnteojoDetailView
from clientes.views import ClienteListView, ClienteUpdateView, ClienteDeleteView, ClienteDetailView
from login import views
from django.conf import settings
from django.conf.urls.static import static
from login.views import LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('anillos/', anillos_views.anillo_form, name='anillo_form'),
    path('pagina_inicio/', anillos_views.pagina_inicio, name= 'acerca_de_mi'),
    path('anteojos/', anteojos_views.anteojo_form, name='anteojo_form'),
    path('clientes/', clientes_views.cliente_form, name='cliente_form'),
    
    path('anillos_lista/', AnilloListView.as_view() , name='anillos_lista'),
    path('anillos_detalle/<pk>', AnilloDetailView.as_view(), name = "anillos_detalle"),
    path('anillos/<pk>/editar', AnilloUpdateView.as_view() , name = "anillos_editar"),
    path('anillos/<pk>/borrar', AnilloDeleteView.as_view(), name = "anillos_borrar"),
    
    path('anteojos_lista/', AnteojoListView.as_view() , name='anteojos_lista'),
    path('anteojos_detalle/<pk>', AnteojoDetailView.as_view(), name = "anteojos_detalle"),
    path('anteojos/<pk>/editar', AnteojoUpdateView.as_view() , name = "anteojos_editar"),
    path('anteojos/<pk>/borrar', AnteojoDeleteView.as_view(), name = "anteojos_borrar"),

    path('clientes_lista/', ClienteListView.as_view() , name='clientes_lista'),
    path('clientes_detalle/<pk>', ClienteDetailView.as_view(), name = "clientes_detalle"),
    path('clientes/<pk>/editar', ClienteUpdateView.as_view() , name = "clientes_editar"),
    path('clientes/<pk>/borrar', ClienteDeleteView.as_view(), name = "clientes_borrar"),

    path('login/', views.login_request, name="login"),
    path('registro/', views.register, name="registro"),
    path('logout/', LogoutView.as_view() , name="logout"),
    

]+ static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)




