
from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView




urlpatterns = [
    path('', home, name="home"),
    path('Stock/', Stock, name="Stock"),
    path('Carrito/', Carrito, name="Carrito"),
    
    #__________LOGIN/LOGOUT/REGISTER:
    
    path('SignUp/', signUp, name="SignUp"),
    path('login/', loginRequest, name="login"),
    path('logout/', LogoutView.as_view(template_name="productos/login.html"), name="logout"),
    

    #FORMS:
    
    path('pantForm/', pant_form, name="pantForm"),
    path('shirtForm/', shirt_form, name="shirtForm"),
    path('buzoForm/', buzo_form, name="buzoForm"),
    
    #UPDATES:
    
    path('pantUpdate/<id_pant>/', pantUpdate, name="pantUpdate"),
    path('shirtUpdate/<id_shirt>/', shirtUpdate, name="shirtUpdate"),
    path('buzoUpdate/<id_buzo>/', buzoUpdate, name="buzoUpdate"),
    
    #DELETES:
    
    path('pantDelete/<id_pant>/', pantDelete, name="pantDelete"),
    path('shirtDelete/<id_shirt>/', shirtDelete, name="shirtDelete"),
    path('buzoDelete/<id_buzo>/', buzoDelete, name="buzoDelete"),
    
    #EDITPROFILE:
    
    path('profile/', editUser, name="profile"),
    path('<int:pk>/password/', changePassword.as_view(), name="changePassword"),
    path('inputAvatar/', inputAvatar, name="inputAvatar"),
  
    #path('StockForm/', StockForm, name="StockForm"),
    #path('Add_product_Success/', success_view, name='successproduct'),
    #path('', home, name="index")
]
