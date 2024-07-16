from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.contenttypes.models import ContentType
from .models import *
from .forms import *

models
# Create your views here.
def home(request):
    return render(request, "productos/index.html")

def Stock(request):
    #contexto = {"Stock" : [pant.objects.all(), buzo.objects.all(), shirt.objects.all()] }
    return render(request, "productos/stock.html")

def Carrito(request):
    return render(request, "productos/carrito.html")

def signup(request):
    if request.method == 'POST':

        form = signup(request.POST)

        if form.is_valid():
            pass  
    else:

        form = SignUp()

    

    return render(request, 'productos/signup.html', {'form': form})



def SignIn(request):
    return render(request, "productos/signin.html")


def stock_form(request):
    miForm = StockForm(request.POST or None)
    model_form = None
    
    if request.method == "POST" and miForm.is_valid():
        producto = miForm.cleaned_data.get('producto')
        
        if producto == 'Pant':
            model_form = pantForm(request.POST or None)
        elif producto == 'Shirt':
            model_form = shirtForm(request.POST or None)
        elif producto == 'Buzo':
            model_form = buzoForm(request.POST or None)
        
        if model_form and model_form.is_valid():
            model_form.save()
            # Renderiza una página de éxito o redirige según tu lógica
    
    contexto = {
        'miForm': miForm,  # Corrige el nombre en el contexto
        'model_form': model_form
    }
    
    return render(request, 'productos/StockForm.html', contexto)



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


