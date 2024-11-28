from django import forms
from django.contrib.auth.forms import AuthenticationForm
from .models import User, Designation, Team

class AddUserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter Password'}))
    first_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter First Name'}))
    last_name = forms.CharField(widget=forms.TextInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter Last Name'}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={'class' : 'form-control text-dark ps-5 h-55', 'placeholder' : 'Enter Email'}))
    deg = forms.ModelChoiceField(queryset=Designation.objects.none(), required=True, label='Designation', widget=forms.Select(attrs={'class' : 'form-select form-control h-55'}))

    class Meta:
        model = User
        fields =['first_name', 'last_name', 'email', 'password']

    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)
        super(AddUserForm, self).__init__(*args, **kwargs)

        if user is not None:
            self.fields['deg'].queryset = Designation.objects.filter(team=Team.objects.get(user=user))

    

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.EmailInput(attrs={'placeholder' : 'Email', 'class': 'form-control h-55'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder' : 'Password', 'class': 'form-control h-55'}))