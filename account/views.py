""" A document with all views """
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render

from account.forms import LoginForm, UserRegistrationForm


@login_required
def dashboard(request):
    """ View page of dashboard"""
    return render(request, 'account/dashboard.html', {'section': 'dashboard'})


def user_login(request):
    """ View page of login"""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            cleaned_data = form.cleaned_data
            user = authenticate(request,
                                username=cleaned_data['username'],
                                password=cleaned_data['password'])
        if user is not None:
            if user.is_active:
                login(request, user)
                return HttpResponse('Authenticated successfully')
            return HttpResponse('Disabled account')
        return HttpResponse('Invalid login')
    form = LoginForm()
    return render(request, 'account/login.html', {'form': form})


def register(request):
    """ User registration view """
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = user_form.save(commit=False)
            new_user.set_password(user_form.cleaned_data['password'])
            new_user.save()
            return render(request, 'account/register_done.html', {'new_user': new_user})
    else:
        user_form = UserRegistrationForm()
    return render(request, 'account/register.html', {'user_form': user_form})
