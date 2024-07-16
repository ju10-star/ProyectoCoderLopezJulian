from django import forms 
from .models import buzo, pant, shirt



class StockForm(forms.Form):
    PRODUCT_CHOICES = [
        ('pant', 'Pant'),
        ('buzo', 'Buzo'),
        ('shirt', 'Shirt'),]
    producto = forms.ChoiceField(choices=PRODUCT_CHOICES, required=True, widget=forms.Select(attrs={'class': 'form-control'}))
    #producto = forms.CharField(max_length=60, required=True)
        
class pantForm(forms.ModelForm):
    class Meta:
            model = pant
            fields = "__all__"
        
class shirtForm(forms.ModelForm): 
    class Meta:
                model = shirt
                fields = "__all__" 
                
class buzoForm(forms.ModelForm): 
    class Meta:
                model = buzo
                fields = "__all__"
    
    
            
            
        
    #modelo = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #talle = forms.CharField(max_length=60, required=True, widget=forms.TextInput(attrs={'class': 'form-control'}))
    #medidas = forms.DecimalField(max_digits=10, decimal_places=2)
    #precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True, widget=forms.NumberInput(attrs={'class': 'form-control'}))
    

class SignUp(forms.Form):
    username = forms.CharField(label='Nombre de usuario', max_length=100)
    email = forms.EmailField(label='Direccion de E-Mail: ')
    password = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    confirm_password = forms.CharField(label='Confirmar contraseña', widget=forms.PasswordInput)
    
    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')
        
        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('Las contraseñas no coinciden.')
        
        return cleaned_data
    