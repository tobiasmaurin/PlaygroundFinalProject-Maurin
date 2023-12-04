from django.shortcuts import render
from anteojos.forms import AnteojoForm

def anteojo_form(request):
    if request.method == 'POST':
        form = AnteojoForm(request.POST)
        if form.is_valid():        
            form.save()
            
    else:
        form = AnteojoForm()
    return render(request, 'anteojos/anteojo_form.html', {'form': form})






