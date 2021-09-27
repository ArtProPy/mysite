""" Account admin """
from django.contrib import admin

from account.models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    """ Class profile admin """
    list_display = ['user', 'date_of_birth', 'photo']
