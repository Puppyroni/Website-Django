from django import forms

class LoginForm(forms.Form):
    input_username = forms.CharField(
        label = 'Nome de Utilizador',
        required = True,
        max_length = 100,
        
        widget = forms.TextInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Ex.: Ricardo Mourão'
            }
        ))
    
    input_password = forms.CharField(
        label = 'password',
        required = True,
        max_length = 50,
        
        widget = forms.PasswordInput(
            attrs = {
                'class': 'form-control',
                'placeholder': 'Please write a password'
            }
        ))