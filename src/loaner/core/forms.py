from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from item.models import User


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter your email address',}))
    
    password = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Password',}))


class SignupForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('name', 'email', 'aadhar_id', 'annual_income' , 'password1', 'password2',)
    
    name = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Username',}))
    
    email = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Email Address',}))
    
    aadhar_id = forms.CharField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Aadhar Id',}))
    
    annual_income = forms.DecimalField(widget=forms.TextInput(
        attrs={'class': 'form-control',
               'placeholder': 'Annual Income',}))
    
    password1 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Enter Password',}))
    
    password2 = forms.CharField(widget=forms.PasswordInput(
        attrs={'class': 'form-control',
               'placeholder': 'Confirm your password',}))