from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.contrib.auth.views import LogoutView





# Create your views here.

#### LOG IN ####
def login_request(request):


    if request.method == 'POST':
        form = AuthenticationForm(request, data = request.POST)
        
        if form.is_valid():  
            usuario = form.cleaned_data.get('username')
            contrasenia = form.cleaned_data.get('password')


            user = authenticate(username= usuario, password=contrasenia)


            login(request, user)
            return render(request, "login/login.html", {"mensaje": f'Bienvenido {user.username}'})



    else:
        form = AuthenticationForm()


    return render(request, "login/login.html", {"form": form})



#### REGISTRO ####

def register(request):

      if request.method == 'POST':

            form = UserCreationForm(request.POST)
            
            if form.is_valid():

                  username = form.cleaned_data['username']
                  form.save()
                  return render(request,"login/login.html" ,  {"mensaje":"Usuario Creado :)"})

      else:
            form = UserCreationForm()
            

      return render(request,"login/registro.html" ,  {"form":form})


### LOG OUT ###
class logout(LogoutView):
     template_name = 'login/logut.html'



