from django.shortcuts import render
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
    if request.method == "POST":
        miForm = StockForm(request.POST)
        if miForm.is_valid():
            # Procesar los datos del formulario
            pass
    else:
        miForm = StockForm()  # Formulario vacío para GET
    return render(request, "productos/StockForm.html", {"form": miForm})
