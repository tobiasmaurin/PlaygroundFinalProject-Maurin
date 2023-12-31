from django.shortcuts import render
from anillos.forms import AnilloForm
from anillos.models import anillo
from django.views.generic import ListView, CreateView, UpdateView, DeleteView, DetailView
from django.urls import reverse_lazy
from django.views.generic.detail import DetailView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator


@login_required(login_url='login')
def anillo_form (request):
    if request.method == 'POST':
        form = AnilloForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = AnilloForm()
    return render(request, 'anillos/anillo_form.html', {'form': form})

####### CRUD DE ANILLOS ##########
@method_decorator(login_required(login_url='login'), name='dispatch')
class AnilloListView(ListView):
    model = anillo
    context_object_name = "anillos"
    template_name = "anillos/anillos_lista.html"



class AnilloDetailView(DetailView):
    model = anillo
    template_name = "anillos/anillos_detalle.html"



class AnilloUpdateView(UpdateView):                                                 
    model = anillo
    template_name = "anillos/anillos_editar.html"
    success_url = reverse_lazy('anillos_lista')
    fields = ['tipo', 'material', 'medida', 'precio', 'imagen']
    



class AnilloDeleteView(DeleteView):
    model = anillo
    template_name = "anillos/anillos_borrar.html"
    success_url = reverse_lazy('anillos_lista')


    ### DESCRIPCION DE LA PAGINA ###
    

def pagina_inicio(request):
    return render(request, 'anillos/acerca_de_mi.html')














# Create your views here.


#def crear_anillo (request):
#    producto = anillo(tipo= 'compromiso', material= 'oro', medida= '15', precio= '70000'  )
#    producto.save()


