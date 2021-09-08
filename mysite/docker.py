

import os

from mysite.setting import *

EMAIL_HOST = os.getenv('EMAIL_HOST', 'localhost')
EMAIL_HOST_USER = os.getenv('EMAIL_HOST_USER', '')
EMAIL_HOST_PASSWORD = os.getenv('EMAIL_HOST_PASSWORD', '')
EMAIL_POST = os.getenv('EMAIL_POST',)
EMAIL_USE_TLS = os.getenv('EMAIL_USE_TLS', True)