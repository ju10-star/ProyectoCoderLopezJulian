from django import forms 

class StockForm(forms.Form):
    producto = forms.CharField(max_length=60, required=True)
    modelo = forms.CharField(max_length=60, required=True)
    talle = forms.CharField(max_length=60, required=True)
    #medidas = forms.DecimalField(max_digits=10, decimal_places=2)
    precio = forms.DecimalField(max_digits=10, decimal_places=2, required=True)
    

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
    