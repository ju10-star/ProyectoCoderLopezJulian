from django import forms 
from .models import buzo, pant, shirt
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm


class pantForm(forms.Form):
    modelo = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    talle = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
class shirtForm(forms.Form):
    modelo = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    talle = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
  
class buzoForm(forms.Form):
    modelo = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    talle = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    
class SignUpForm(UserCreationForm):
    email = forms.EmailField(required=True)
    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="confirme su contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]
        
class UserEditForm(UserChangeForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(label="User Name", max_length=50, required=True)
    last_name = forms.CharField(label="Last name", max_length=50, required=True)

    class Meta:
        model = User
        fields = ["email", "first_name", "last_name"]
        
class AvatarForm(forms.Form):
    avatar = forms.ImageField(required=True)

#class StockForm(forms.Form):
    #PRODUCT_CHOICES = [
        #('pant', 'Pant'),
        #('buzo', 'Buzo'),
        #('shirt', 'Shirt'),]
    #producto = forms.ChoiceField(choices=PRODUCT_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
        
#class pantForm(forms.ModelForm):
    #class Meta:
            #model = pant
            #fields = "__all__"
        
#class shirtForm(forms.ModelForm): 
    #class Meta:
                #model = shirt
                #fields = "__all__" 
                
#class buzoForm(forms.ModelForm): 
    #class Meta:
                #model = buzo
                #fields = "__all__"
    
    
            
            
        
    #modelo = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #talle = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    

