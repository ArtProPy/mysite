"""
Module indented to extend and override settings.py via the environment
variables.
"""

import os

from mysite.settings import *  # pylint: disable=unused-wildcard-import,wildcard-import

EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_POST = os.getenv('EMAIL_POST', '')
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', '').lower() == 'true'
