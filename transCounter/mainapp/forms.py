from django import forms
from django.forms.widgets import PasswordInput

class LoginForm(forms.Form):
    username = forms.CharField(label='username')
    password = forms.CharField(label='password', widget=PasswordInput)