from django import forms
from .models import *
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

class FeedBack_form (forms.ModelForm):
    class Meta:
        model = Data_message
        fields = ['email', 'message']
        widgets = {
            'email': forms.TextInput(attrs={'class':'form-input'}),
            'message': forms.Textarea(attrs={'cols':120, 'rows':20})
        }

class RegisterUserForm (UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput (attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput (attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput (attrs={'class': 'form-input'}))

    class Meta:
        model = User
        fields =('username', 'password1','password2')
        
class LoginUserForm (AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput (attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput (attrs={'class': 'form-input'}))