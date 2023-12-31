from django.shortcuts import render
from clientes.forms import ClienteForm
from clientes.models import cliente
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator



@login_required(login_url='login')
def cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():        
            form.save()
            
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

# Create your views here.

##### CRUD #####
@method_decorator(login_required(login_url='login'), name='dispatch')
class ClienteListView(ListView):
    model = cliente
    context_object_name = "clientes"
    template_name = "clientes/clientes_lista.html"



class ClienteDetailView(DetailView):
    model = cliente
    template_name = "clientes/clientes_detalle.html"


class ClienteUpdateView(UpdateView):
    model = cliente
    template_name = "clientes/clientes_editar.html"
    success_url = reverse_lazy('clientes_lista')
    fields = ['nombre', 'dni', 'email', 'celular', 'imagen']
    


class ClienteDeleteView(DeleteView):
    model = cliente
    template_name = "clientes/clientes_borrar.html"
    success_url = reverse_lazy('clientes_lista')