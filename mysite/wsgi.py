"""
WSGI config for mysite project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/wsgi/
"""

import os
from dotenv import load_dotenv
from django.core.wsgi import get_wsgi_application
from settings import BASE_DIR

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
project_folder = os.path.expanduser(BASE_DIR)
load_dotenv(os.path.join(project_folder,'.env'))
application = get_wsgi_application()
