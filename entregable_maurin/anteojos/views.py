from django.shortcuts import render
from anteojos.forms import AnteojoForm
from anteojos.models import anteojo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required(login_url='login')
def anteojo_form(request):
    if request.method == 'POST':
        form = AnteojoForm(request.POST)
        if form.is_valid():        
            form.save()
            
    else:
        form = AnteojoForm()
    return render(request, 'anteojos/anteojo_form.html', {'form': form})

######### CRUD #########
@method_decorator(login_required(login_url='login'), name='dispatch')
class AnteojoListView(ListView):
    model = anteojo
    context_object_name = "anteojos"
    template_name = "anteojos/anteojos_lista.html"


class AnteojoDetailView(DetailView):
    model = anteojo
    template_name = "anteojos/anteojos_detalle.html"


class AnteojoUpdateView(UpdateView):
    model = anteojo
    template_name = "anteojos/anteojos_editar.html"
    success_url = reverse_lazy('anteojos_lista')
    fields = ['tipo', 'marca', 'color', 'tamanio', 'fecha_de_venta', 'imagen']
    


class AnteojoDeleteView(DeleteView):
    model = anteojo
    template_name = "anteojos/anteojos_borrar.html"
    success_url = reverse_lazy('anteojos_lista')




