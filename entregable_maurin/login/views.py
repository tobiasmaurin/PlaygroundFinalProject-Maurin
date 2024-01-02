from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from .models import PerfilUsuario
from django.urls import reverse_lazy






# Create your views here.

#### LOG IN ####
def login_request(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        
        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')

            user = authenticate(username=usuario, password=contrasenia)

            if user is not None:
                login(request, user)
                return render(request, "login/login.html", {"mensaje": f'Bienvenido {user.username}'})
    
    else:
        form = AuthenticationForm()

    return render(request, "login/login.html", {"form": form})

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            
            # Crear un perfil para el usuario registrado
            PerfilUsuario.objects.create(usuario=user)
            
            return render(request, "login/login.html", {"mensaje": "Usuario Creado :)"})
    
    else:
        form = UserCreationForm()

    return render(request, "login/registro.html", {"form": form})

### LOG OUT ###
class logout(LogoutView):
     template_name = 'login/logut.html'
     success_url = reverse_lazy('login')



