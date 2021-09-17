""" Configuration of account forms """
from django import forms


class LoginForm(forms.Form):
    """ Form for login """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)
