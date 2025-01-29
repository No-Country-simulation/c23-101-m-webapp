from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class CustomUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username','password1','password2','email')
        widgets= {
            'username': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'password1': forms.PasswordInput(attrs={'class': 'form-control'}),
            'password2': forms.PasswordInput(attrs={'class': 'form-control'})
        }
        
        error_messages = {
            'password1': {
                'required': 'Este campo es obligatorio.',
                'min_length': 'La contraseña debe tener al menos 8 caracteres.',
                'max_length': 'La contraseña no puede tener más de 128 caracteres.',
                'invalid': 'La contraseña contiene caracteres no válidos.',
            },
            
            'password2': {
                'password_mismatch': 'Las contraseñas no coinciden.',
            },
            
            'username': {
                'unique': 'Este nombre de usuario ya está en uso.'
            }            
        }