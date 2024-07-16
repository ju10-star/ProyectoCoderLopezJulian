
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', home, name="home"),
    path('Stock/', Stock, name="Stock"),
    path('Carrito/', Carrito, name="Carrito"),
    path('SignUp/', signup, name="SignUp"),
    path('SignIn/', SignIn, name="SignIn"),
    path('StockForm/', stock_form, name="StockForm"),
    path('Add_product_Success/', success_view, name='successproduct'),
    #path('', home, name="index")
]
