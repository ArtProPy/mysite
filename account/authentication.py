""" Authentication user's """
from django.contrib.auth.models import User


class EmailAuthBackend:
    """ Auth user for e-mail"""
    @staticmethod
    def authenticate(request, username=None, password=None):
        """ Auth user's """
        try:
            user = User.objects.get(email=username)
            if user.check_password(password):
                return user
            return None
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user(user_id):
        """ Get user """
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None
