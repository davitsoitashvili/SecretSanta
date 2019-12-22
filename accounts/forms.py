from django import forms
from accounts.models import User
from accounts.CustomForm import UserCreationForm,SignInForm



class UserForm(UserCreationForm):
    name = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    surname = forms.CharField(widget=forms.TextInput(attrs={"class": "form-control"}))
    email = forms.EmailField(widget=forms.EmailInput(attrs={"class": "form-control"}))
    age = forms.IntegerField(widget=forms.NumberInput(attrs={"class": "form-control"}))
    password1 = forms.CharField(label="Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))
    password2 = forms.CharField(label="Confirmation Password", widget=forms.PasswordInput(attrs={"class": "form-control"}))

    class Meta:
        model = User
        fields = ['email','name', 'surname', 'age','password1', 'password2']

class LoginForm(SignInForm):
    class Meta:
        model = User
        fields = ['email', 'password1', 'password2']

