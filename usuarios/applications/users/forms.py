from django import forms
from django.contrib.auth import authenticate

from .models import User

class UserRegisterForm(forms.ModelForm):

    password1 = forms.CharField(label='Contraseña', 
    required=True,
    widget=forms.PasswordInput(
        attrs={
            'placeholder':'Contraseña'
        }
    ))

    password2 = forms.CharField(label='Contraseña', 
    required=True,
    widget=forms.PasswordInput(
        attrs={
            'placeholder':'Repetir contraseña'
        }
    ))


    class Meta:

        model = User
        fields = (
            'username',
            'email',
            'nombres',
            'apellidos',
            'genero',

        )

    def clean_password2(self):
        if self.cleaned_data['password1'] != self.cleaned_data['password2']:
            self.add_error('password2', 'Las cotraseñas no son iguales')
    
    def clean_password1_password2(self):
        if self.cleaned_data['password1'] <=6 and self.cleaned_data['password2'] <=6:
            self.add_error('Las contraseña menor a 6 caracteres')



class LoginForm(forms.Form):

    username = forms.CharField(
        label='username', 
        required=True,
        widget=forms.TextInput(
        attrs={
            'placeholder':'Contraseña'
        }
    ))

    password = forms.CharField(label='Contraseña', 
        required=True,
        widget=forms.PasswordInput(
        attrs={
            'placeholder':'contraseña'
        }
    ))


    def clean(self):
        cleaned_data = super(LoginForm, self).clean()
        username = self.cleaned_data['username'] 
        password =  self.cleaned_data['password']
        
        if not authenticate(username=username, password=password):
            raise forms.ValidationError('no son correctos los datos del usaurio')

        return self.cleaned_data
        


class UpdatePasswordForm(forms.Form):

    password1 = forms.CharField(
    label='Contraseña', 
    required=True,
    widget=forms.PasswordInput(
        attrs={
            'placeholder':'Contraseña actual'
        }
    ))

    password2 = forms.CharField(label='Contraseña', 
    required=True,
    widget=forms.PasswordInput(
        attrs={
            'placeholder':'Contraseña nueva'
        }
    ))