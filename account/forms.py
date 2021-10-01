""" Configuration of account forms """
from django import forms
from django.contrib.auth.models import User

from account.models import Profile


class LoginForm(forms.Form):
    """ Form for login """
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class ProfileEditForm(forms.ModelForm):
    """ Profile edit form """
    class Meta:
        """ Meta profile edit form"""
        model = Profile
        fields = ('date_of_birth', 'photo')
        widgets = {
            'date_of_birth': forms.DateInput(format='%d-%m-%Y'),
        }


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
        cleaned_data = self.cleaned_data
        if cleaned_data['password'] != cleaned_data['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cleaned_data['password2']

    def clean_email(self):
        """ Verifying the identity of passwords """
        cleaned_data = self.cleaned_data
        if len(User.objects.get(cleaned_data['email'])):
            raise forms.ValidationError('The user with this email already exists')
        return cleaned_data['email']
