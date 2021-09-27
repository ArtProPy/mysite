""" Configuration of account forms """
from django import forms
from django.contrib.auth.models import User


class LoginForm(forms.Form):
    """ Form for login """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserEditForm(forms.ModelForm):
    """ User edit form """
    class Meta:
        """ Meta user edit form """
        model = User
        fields = ('first_name', 'last_name', 'email')


class UserRegistrationForm(forms.ModelForm):
    """ User registration form """
    password = forms.CharField(label='Password', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password', widget=forms.PasswordInput)

    class Meta:
        """ Meta user registration form """
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        """ Verifying the identity of passwords """
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


"""
class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('date_of_birth', 'photo')
"""