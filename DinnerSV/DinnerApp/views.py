from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .models import *
from .models import User as us
from .forms import *
from django.contrib import messages
# Create your views here.


def index(request):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"



    data ={
        "imgindex":"DinnerApp/img/img1.jpg",
        "cliente": cliente,
        "gerente" : gerente,
    }
    return render(request, 'DinnerApp/index.html',data)


def profile(request):
    return render(request, 'DinnerApp/profile.html')

def loginuser(request):

    if request.method == "POST":
        email = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=email, password=password )
        if user is not None:
            login(request, user)
            type_obj = user_type.objects.get(user=user)
            if user.is_authenticated and type_obj.es_cliente:
                return redirect('home')
            elif user.is_authenticated and type_obj.es_gerente:
                return redirect('home')
            else:
                return redirect('home')
        else:
            messages.success(request, ("Ups!, hubo un error iniciando sesion."))
            return redirect('home')
        


    data = {
        "Title":"Login",
        "css": "DinnerApp/css/login.css",
    }
    return render(request, 'registration/login.html',data)

def logoutuser(request):
    logout(request)
    messages.success(request,("has cerrado sesion!"))
    return redirect('home')

def register(request):

    form = UserRegisterForm()
    
    if (request.method == 'POST'):
        form = UserRegisterForm(request.POST)
        email = request.POST.get('username')
        password = request.POST.get('password1')
        tipo_usuraio = request.POST.get('tipo')
        numero = request.POST.get('numero')
        nombre = request.POST.get('Nombre')
        
        user = us.objects.create_user(
            email=email,name=nombre,numero=numero,
        )
        user.set_password(password)
        user.save()
        
        usert = None
        if tipo_usuraio == '2' :
            usert = user_type(user=user,es_cliente=True)
        elif tipo_usuraio == '1':
            usert = user_type(user=user,es_gerente=True)
        
        usert.save()
        user = authenticate(request,username=email,password=password)
        login(request,user)
        #Successfully registered. Redirect to homepage
          
        return redirect('home')

    data = {'form':form}
    return render(request, "DinnerApp/register.html", data)

def viewRestaurantes(request):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"



    restaurante = Restaurante.objects.all()
    data = {
        'restaurantes' : restaurante,
        'css' : 'DinnerApp/css/restaurantes.scss',
        "cliente": cliente,
        "gerente" : gerente,
    }
    return render(request, 'DinnerApp/restaurantes.html',data)

def viewPerfilCliente(request):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"

    data = {
        'css' : 'DinnerApp/css/perfil.css',
        'tittle':'Mi Perfil',
        "cliente": cliente,
        "gerente" : gerente,
    }
    return render(request, 'DinnerApp/cprofile.html',data)

def viewPerfilGerente(request):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"

    data = {
        'css' : 'DinnerApp/css/perfil.css',
        'tittle':'Mi Perfil',
        "cliente": cliente,
        "gerente" : gerente,
    }
    return render(request, 'DinnerApp/gprofile.html',data)

def Reservar(request, id):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"


    restauranteid = Restaurante.objects.get(id=id)



    form = reservacionForm(restauranteid=restauranteid)

    def get_form_kwargs(self):
        """ Passes the request object to the form class.
         This is necessary to only display members that belong to a given user"""

        kwargs = super(Reservar, self).get_form_kwargs()
        kwargs['restauranteid'] = self.restauranteid
        return kwargs    


    if (request.method == "POST"):
        form = reservacionForm(data=request.POST,restauranteid=restauranteid)
        reservacion=Reservacion(
            restaurante=restauranteid,
            usuario=request.user,
            hora=request.POST.get('horario'),
            menu=Menu.objects.get(id=request.POST.get('menu'))
        )
        reservacion.save()
        form=''
        return redirect('home')


    
    data= {
        'form': form,
        'tittle': 'Reservar',
        "cliente": cliente,
        "gerente" : gerente,
    }

    return render(request, 'DinnerApp/reservar.html',data)
# def restaurantes(request):
def Reservaciones(request):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"

    resevacion = Reservacion.objects.filter(usuario=current_user)
    data = {
    'reservaciones': resevacion,
    "cliente": cliente,
    "gerente" : gerente,
    }

    return render(request,'DinnerApp/reservaciones.html',data)

def agregarRestaurante(request):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"

    form = restauranteForm()
    if (request.method == 'POST'):
        form = restauranteForm(request.POST)
        restaurante=Restaurante(
            nombre = request.POST.get('nombre'),
            correo = request.POST.get('correo'),
            descripcion = request.POST.get('descripcion'),
            categoria = request.POST.get('categoria'),
            telefono = request.POST.get('telefono'),
            ciudad = request.POST.get('ciudad'),
            direccion = request.POST.get('direccion'),
            capacidad = request.POST.get('capacidad'),
            redesSociales = request.POST.get('redesSociales'),
            paginaWeb = request.POST.get('paginaWeb'),
            gerente= request.user
        )
        restaurante.save()
        form=''
        return redirect('/gperfil')
    data={
        'form':form,
        "cliente": cliente,
        "gerente" : gerente,

    }
    return render(request,'DinnerApp/CrearRestaurante.html',data)


def addmenu(request):

    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"


    form = menuForm(request=request)
    if (request.method == "POST"):
        form = menuForm(data=request.POST,request=request)
        menu=Menu(
            nombre=request.POST.get('nombre'),
            descripcion=request.POST.get('descripcion'),
            restaurante=Restaurante.objects.get(id=request.POST.get('restaurante'))
        )
        menu.save()
        form = ''
        return redirect('gPerfil')
    data ={
        'form':form,
        "cliente": cliente,
        "gerente" : gerente,
    }

    return render(request, 'DinnerApp/amenu.html',data)

def viewRestauranteG(request):
    current_user = request.user
    gerente = False
    cliente = False

    if current_user.is_authenticated:
        if user_type.objects.get(user = current_user).es_cliente:
            cliente = "True"
            gerente = "False"
        elif user_type.objects.get(user = current_user).es_gerente:
            gerente = "True"
            cliente = "False"

    restaurante = Restaurante.objects.filter(gerente=current_user)
    data = {
        'restaurantes' : restaurante,
        'css' : 'DinnerApp/css/restaurantes.scss',
        "cliente": cliente,
        "gerente" : gerente,
    }
    return render(request, 'DinnerApp/grestaurantes.html',data)
