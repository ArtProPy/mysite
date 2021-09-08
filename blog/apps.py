""" Config apps """
from django.apps import AppConfig


class BlogConfig(AppConfig):
    """ Config blog"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'blog'
