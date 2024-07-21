from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from django.urls import reverse_lazy

from .models import *
from .forms import *

from django.views.generic import ListView
from django.views.generic import CreateView
from django.views.generic import UpdateView
from django.views.generic import DeleteView

from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import PasswordChangeView



from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required



# Create your views here.
def home(request):
    return render(request, "productos/index.html")

def Stock(request):
    #contexto = {"Stock" : [pant.objects.all(), buzo.objects.all(), shirt.objects.all()] }
    return render(request, "productos/stock.html")

def Carrito(request):
    return render(request, "productos/carrito.html")

def signUp(request):
    if request.method == "POST":
        miForm = SignUpForm(request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get("username")
            miForm.save()
            return redirect(reverse_lazy('home'))
    else:
        miForm = SignUpForm()

    return render(request, "productos/signup.html", {"form": miForm})


def loginRequest(request):
    if request.method == "POST":
        usuario = request.POST["username"]
        clave = request.POST["password"]
        user = authenticate(request, username=usuario, password=clave)
        if user is not None:
            login(request, user)
            try:
                Avatar = avatar.objects.get(user=request.user.id).imagen.url
            except:
                Avatar = "/media/avatares/default.png"
            finally:
                request.session["Avatar"] = Avatar
            return render(request, "productos/index.html")
        else:
            return redirect(reverse_lazy('login'))
    else:
        miForm = AuthenticationForm()

    return render(request, "productos/login.html", {"form": miForm})






#__________FORMS:

@login_required
def pant_form(request):
    if request.method == "POST":
        miForm = pantForm(request.POST)
        if miForm.is_valid():
            form_modelo = miForm.cleaned_data.get('modelo')
            form_talle = miForm.cleaned_data.get('talle')
            form_precio = miForm.cleaned_data.get('precio')
            pants = pant(modelo=form_modelo, talle=form_talle, precio=form_precio)
            pants.save()
            miForm = pantForm()
            contexto = {"pants" : pant.objects.all(), 'miForm' : miForm}
            return render(request, "productos/StockForm.html", contexto)
    else:
        miForm = pantForm()
    #pants = {"pants" : pant.objects.all()}
    pants = pant.objects.all()
    return render(request, "productos/StockForm.html", {'miForm' : miForm, 'pants' : pants})
    #pants = pant.objects.all()
    #contexto = {'miForm' : miForm}
    #return render(request, "productos/StockForm.html", contexto, {'pants' : pants})

@login_required
def shirt_form(request):
    if request.method == "POST":
        miForm = shirtForm(request.POST)
        if miForm.is_valid():
            form_modelo = miForm.cleaned_data.get('modelo')
            form_talle = miForm.cleaned_data.get('talle')
            form_precio = miForm.cleaned_data.get('precio')
            Shirt = shirt(modelo=form_modelo, talle=form_talle, precio=form_precio)
            Shirt.save()
            miForm = shirtForm()
            contexto = {"shirts" : shirt.objects.all(), 'miForm' : miForm}
            return render(request, "productos/shirtForm.html", contexto)
    else:
        miForm = shirtForm()
    shirts = shirt.objects.all()
    return render(request, "productos/shirtForm.html", {'miForm' : miForm, 'shirts' : shirts})

@login_required
def buzo_form(request):
    if request.method == "POST":
        miForm = buzoForm(request.POST)
        if miForm.is_valid():
            form_modelo = miForm.cleaned_data.get('modelo')
            form_talle = miForm.cleaned_data.get('talle')
            form_precio = miForm.cleaned_data.get('precio')
            Buzo = buzo(modelo=form_modelo, talle=form_talle, precio=form_precio)
            Buzo.save()
            miForm = buzoForm()
            contexto = {"buzos" : buzo.objects.all(), 'miForm' : miForm}
            return render(request, "productos/buzoForm.html", contexto)
    else:
        miForm = buzoForm()
    buzos = buzo.objects.all()
    return render(request, "productos/buzoForm.html", {'miForm' : miForm, 'buzos' : buzos})

#_______________EDITPROFILE:


@login_required
def editUser(request):
    usuario = request.user
    if request.method == "POST":
        miForm = UserEditForm(request.POST)
        if miForm.is_valid():
            user = User.objects.get(username=usuario)
            user.email = miForm.cleaned_data.get("email")
            user.username = miForm.cleaned_data.get("username")
            user.username = miForm.cleaned_data.get("username")
            user.save()
            return redirect(reverse_lazy("home"))
    else:
        miForm = UserEditForm(instance=usuario)
    return render(request, "productos/profile.html", {"form": miForm})


class changePassword(LoginRequiredMixin, PasswordChangeView):
    template_name = "productos/changePassword.html"
    success_url = reverse_lazy("home")
    
@login_required   
def inputAvatar(request):
    if request.method == "POST":
        miForm = AvatarForm(request.POST, request.FILES)
        if miForm.is_valid():
            usuario = User.objects.get(username=request.user)
            old_avatar = avatar.objects.filter(user=usuario)
            imagen = miForm.cleaned_data["imagen"]
            if len(old_avatar) > 0:
                for i in range(len(old_avatar)):
                    old_avatar[i].delete()
            Avatar = avatar(user=usuario, imagen=imagen)
            Avatar.save()
            imagen = avatar.objects.get(user=usuario).imagen.url
            request.session["avatar"] = imagen
            return redirect(reverse_lazy("home"))
    else: 
        miForm = AvatarForm()
    return render(request, "productos/addAvatar.html", {"miForm": miForm})


#________________UPDATES:
@login_required
def pantUpdate(request, id_pant):
    Pant = pant.objects.get(id=id_pant)
    if request.method == "POST":
        miForm = pantForm(request.POST)
        if miForm.is_valid():
            Pant.modelo = miForm.cleaned_data.get("modelo")
            Pant.talle = miForm.cleaned_data.get("talle")
            Pant.precio = miForm.cleaned_data.get("precio")
            Pant.save()
            contexto = {"pants": pant.objects.all(), 'miForm' : miForm}
            return render(request, "productos/pantForm.html", contexto)       
    else:
        miForm = pantForm(initial={"modelo": Pant.modelo, 
                                   "talle": Pant.talle, 
                                   "precio": Pant.precio})
    pants = pant.objects.all()
    return render(request, "productos/StockForm.html", {"miForm": miForm, "pants" : pants})


@login_required
def shirtUpdate(request, id_shirt):
    Shirt = shirt.objects.get(id=id_shirt)
    if request.method == "POST":
        miForm = shirtForm(request.POST)
        if miForm.is_valid():
            Shirt.modelo = miForm.cleaned_data.get("modelo")
            Shirt.talle = miForm.cleaned_data.get("talle")
            Shirt.precio = miForm.cleaned_data.get("precio")
            Shirt.save()
            contexto = {"shirts": shirt.objects.all(), 'miForm' : miForm}
            return render(request, "productos/shirtForm.html", contexto)       
    else:
        miForm = shirtForm(initial={"modelo": Shirt.modelo, 
                                    "talle": Shirt.talle, 
                                    "precio": Shirt.precio}) 
    shirts = shirt.objects.all()
    return render(request, "productos/shirtForm.html", {"miForm": miForm, "shirts" : shirts})


@login_required
def buzoUpdate(request, id_buzo):
    Buzo = buzo.objects.get(id=id_buzo)
    if request.method == "POST":
        miForm = buzoForm(request.POST)
        if miForm.is_valid():
            Buzo.modelo = miForm.cleaned_data.get("modelo")
            Buzo.talle = miForm.cleaned_data.get("talle")
            Buzo.precio = miForm.cleaned_data.get("precio")
            Buzo.save()
            miForm = buzoForm()
            contexto = {"buzos": buzo.objects.all(), 'miForm' : miForm}
            return render(request, "productos/buzoForm.html", contexto)       
    else:
        miForm = buzoForm(initial={"modelo": Buzo.modelo, 
                                   "talle": Buzo.talle, 
                                   "precio": Buzo.precio}) 
    buzos = buzo.objects.all()
    return render(request, "productos/buzoForm.html", {"miForm": miForm, "buzos" : buzos})




#________________DELETES:

@login_required
def pantDelete(request, id_pant):
    Pant = pant.objects.get(id=id_pant)
    Pant.delete()
    contexto = {"pants": pant.objects.all() }
    return render(request, "productos/StockForm.html", contexto)

@login_required
def shirtDelete(request, id_shirt):
    Shirt = shirt.objects.get(id=id_shirt)
    Shirt.delete()
    contexto = {"shirts": shirt.objects.all() }
    return render(request, "productos/shirtForm.html", contexto)

@login_required
def buzoDelete(request, id_buzo):
    Buzo = buzo.objects.get(id=id_buzo)
    Buzo.delete()
    contexto = {"buzos": buzo.objects.all() }
    return render(request, "productos/buzoForm.html", contexto)



     
    
    
    



#def stock_form(request):
    #miForm = StockForm(request.POST or None)
    #model_form = None
    
    #if request.method == "POST" and miForm.is_valid():
        #producto = miForm.cleaned_data.get('producto')
        
        #if producto == 'Pant':
            #model_form = pantForm(request.POST or None)
        #elif producto == 'Shirt':
            #model_form = shirtForm(request.POST or None)
        #elif producto == 'Buzo':
            #model_form = buzoForm(request.POST or None)
        
        #if model_form and model_form.is_valid():
            #model_form.save()
    
    #contexto = {
        #'miForm': miForm,  
        #'model_form': model_form}
    
    #return render(request, 'productos/StockForm.html', contexto)



#def stock_form(request):
    #if request.method == 'POST':
        #miForm = StockForm(request.POST)
        #if miForm.is_valid():
            #producto = miForm.cleaned_data['producto']
            
            #if producto == 'pant':
                #model_form = pantForm(request.POST)
            #elif producto == 'shirt':
                #model_form = shirtForm(request.POST)
            #elif producto == 'buzo':
                #model_form = buzoForm(request.POST)
            #else:
                #model_form = None
            
            #if model_form is not None and model_form.is_valid():
                #model_form.save()
                #return render(request, 'success.html')  # Renderiza una página de éxito o redirige según tu lógica
    #else:
        #miForm = StockForm()
        #model_form = None
    
    #return render(request, 'form_template.html', {'miForm': miForm, 'model_form': model_form})


#def stock_form(request):
    #miForm = StockForm(request.POST or None)
    #model_form = None
    #if request.method == "POST" and miForm.is_valid():
        #producto = miForm.cleaned_data.get('producto')    
        #if producto == 'Pant':
            #model_form = pantForm(request.POST or None)
        #elif producto == 'Shirt':
            #model_form = shirtForm(request.POST or None)
        #elif producto == 'Buzo':
            #model_form = buzoForm(request.POST or None)
        #if model_form and model_form.is_valid():
            #model_form.save()
    #contexto = {'stock_form' : miForm,
                #'model_form' : model_form}
    #return render(request, 'productos/StockForm.html', contexto)
    
    
    #else:
        #miForm = StockForm()
        #context = {'form': miForm,}
        #return render(request, 'productos/StockForm.html', context)
        
        

#def stock_form(request):
    #if request.method == "POST":
        #miForm = StockForm(request.POST)
        #if miForm.is_valid():
            #producto = miForm.cleaned_data.get('producto')
            #modelo = miForm.cleaned_data.get('modelo')
            #talle = miForm.cleaned_data.get('talles')
            #precio = miForm.cleaned_data.get('precio')    
            #if producto == 'Pant':
                #Pant = pant(modelo_pant=modelo, talles=talle, precio=precio)
                #Pant.save()
                #contexto = {"producto" : pant.objects.all()}
                #return render(request, 'productos/StockForm.html', contexto)
            #elif producto == 'Shirt':
                #Shirt = shirt(modelo_shirt=modelo, talles=talle, precio=precio)
                #Shirt.save()
                #contexto = {"producto" : shirt.objects.all()}
                #return render(request, 'productos/StockForm.html', contexto)
            #elif producto == 'Buzo':
                #Buzo = buzo(modelo_buzo=modelo, talles=talle, precio=precio)
                #Buzo.save()
                #contexto = {"producto" : buzo.objects.all()}
                #return render(request, 'productos/StockForm.html', contexto)
    #else:
        #miForm = StockForm()
    #context = {'form': miForm,}
    #return render(request, 'productos/StockForm.html', context)

        
        
    

def success_view(request):
    return render(request, "productos/Add_product_Success.html")


