from django.shortcuts import render
from clientes.forms import ClienteForm

def cliente_form(request):
    if request.method == 'POST':
        form = ClienteForm(request.POST)
        if form.is_valid():        
            form.save()
            
    else:
        form = ClienteForm()
    return render(request, 'clientes/cliente_form.html', {'form': form})

# Create your views here.

