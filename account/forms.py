from django import forms
from .models import User

class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter Email'}))
    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email', 'password']