from django.shortcuts import render
from anillos.forms import AnilloForm

def anillo_form (request):
    if request.method == 'POST':
        form = AnilloForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = AnilloForm()
    return render(request, 'anillos/anillo_form.html', {'form': form})














# Create your views here.


#def crear_anillo (request):
#    producto = anillo(tipo= 'compromiso', material= 'oro', medida= '15', precio= '70000'  )
#    producto.save()


