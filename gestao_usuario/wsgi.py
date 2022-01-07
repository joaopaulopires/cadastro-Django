"""
WSGI config for gestao_usuario project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""
# Documentação para o utilitário Static https://pypi.org/project/dj-static/
#Documentação guinicor para o arquivo Procfile https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/gunicorn/
# https://docs.gunicorn.org/en/stable/settings.html

import os

from django.core.wsgi import get_wsgi_application
from dj_static import Cling



os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'gestao_usuario.settings')

application = Cling(get_wsgi_application())
